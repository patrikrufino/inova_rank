from fastapi import APIRouter

from inova_rank_api.schemas import IdeaSchema

router = APIRouter(prefix='/ideas', tags=['ideas'])


@router.post('/')
def create_idea(idea: IdeaSchema):
    return idea
