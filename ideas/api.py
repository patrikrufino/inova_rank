from django.db.models.manager import BaseManager
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination
from ideas.models import Idea
from .schemas import *
from core.utils import Response, MessageResponse, ErrorResponse


ideas_router = Router()

@ideas_router.post('/', response={201: MessageResponse, 400: ErrorResponse, 500: ErrorResponse})
def create_idea(request, data: CreateIdeaSchema) -> Response:
    try:
        name: str = data.dict()['name']
        content: str = data.dict()['content']
        
        if not name or not content:
            return Response('Invalid request', status=400).to_response()
        
        idea = Idea(name=name, content=content)
        idea.save()
        
        return Response('Idea created successfully', status=201, data={"id": idea.id, "name": idea.name, "content": idea.content}).to_response()
    
    except Exception as e:
        return Response('An error occurred while creating the idea.', status=500).to_response()

@ideas_router.get('/', response={200: list[ListAllIdeasSchema], 500: ErrorResponse})
@paginate(PageNumberPagination, page_size=20)
def list_ideas(request) -> Response:
    try:
        ideas: BaseManager[Idea] = Idea.objects.all()  
        return [ListAllIdeasSchema.from_orm(idea) for idea in ideas]  
    
    except Exception as e:
        return Response('An error occurred while retrieving ideas.', status=500).to_response()
    
@ideas_router.get('/{slug}', response={200: IdeaSchema, 404: ErrorResponse, 500: ErrorResponse})
def get_idea(request, slug: str) -> Response:
    try:
        idea: Idea = Idea.objects.get(slug=slug)
        return IdeaSchema.from_orm(idea)
    except Idea.DoesNotExist:
        return Response('Idea not found', status=404).to_response()
    except Exception as e:
        return Response('An error occurred while retrieving the idea.', status=500).to_response()
