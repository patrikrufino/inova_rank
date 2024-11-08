from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from inova_rank_api.database import get_session
from inova_rank_api.models import Category, User
from inova_rank_api.schemas import CategoryIn, CategoryOut, FilterPage
from inova_rank_api.security import get_current_user

router = APIRouter(prefix='/categories', tags=['categories'])

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=CategoryOut)
def create_category(category: CategoryIn, session: T_Session) -> CategoryOut:
    category_db: Category | None = session.scalar(
        select(Category).where(Category.name == category.name)
    )

    if category_db:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Category already exists',
        )

    category_db = Category(name=category.name)
    session.add(category_db)
    session.commit()
    session.refresh(category_db)
    return category_db


@router.get('/', response_model=list[CategoryOut])
def read_categories(
    session: T_Session, filter_users: Annotated[FilterPage, Query()]
) -> list[CategoryOut]:
    categories: list[CategoryOut] = (
        session.execute(
            select(Category)
            .offset(filter_users.offset)
            .limit(filter_users.limit)
        )
        .scalars()
        .all()
    )
    return categories
