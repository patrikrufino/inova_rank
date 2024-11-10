import select
from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from inova_rank_api.database import get_session
from inova_rank_api.models import Category, Idea, User
from inova_rank_api.schemas import FilterPage, IdeaIn, IdeaList, IdeaOut
from inova_rank_api.security import get_current_user

router = APIRouter(prefix='/ideas', tags=['ideas'])

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=IdeaOut)
def create_idea(idea: IdeaIn, session: T_Session) -> IdeaOut:
    idea_db: Idea | None = session.scalar(
        select(Idea).where(Idea.title == idea.title)
    )

    if idea_db:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Idea already exists',
        )

    idea_db = Idea(
        author_id=idea.author_id,
        title=idea.title,
        content=idea.content,
        category_id=idea.category_id,
    )
    session.add(idea_db)
    session.commit()
    session.refresh(idea_db)

    return idea_db


@router.get('/', response_model=IdeaList)
def read_ideas(
    session: T_Session,
    filter_ideas: Annotated[FilterPage, Query()],
) -> IdeaList:
    ideas: IdeaList = session.scalars(
        select(Idea).offset(filter_ideas.offset).limit(filter_ideas.limit)
    ).all()
    return {'ideas': ideas}
