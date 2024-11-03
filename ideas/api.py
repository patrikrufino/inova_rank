from django.db.models.manager import BaseManager
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination
from ideas.models import Idea
from .schemas import CreateIdeaSchema, ListAllIdeasSchema, IdeaSchema
from core.utils import Response, MessageResponse, ErrorResponse

ideas_router = Router()

@ideas_router.post('/', response={201: MessageResponse, 400: ErrorResponse, 500: ErrorResponse})
def create_idea(request, data: CreateIdeaSchema) -> Response:
    try:
        idea = Idea(**data.dict())
        idea.save()
        return Response('Idea created successfully', status=201, data={"id": idea.id, "name": idea.name, "content": idea.content}).to_response()
    
    except Exception as e:
        return Response(f'An error occurred while creating the idea: {str(e)}', status=500).to_response()

@ideas_router.get('/', response={200: list[ListAllIdeasSchema], 500: ErrorResponse})
@paginate(PageNumberPagination, page_size=20)
def list_ideas(request) -> Response:
    try:
        ideas: BaseManager[Idea] = Idea.objects.all() 
        return [ListAllIdeasSchema.from_orm(idea) for idea in ideas] 
    
    except Exception as e:
        return Response(f'An error occurred while retrieving ideas: {str(e)}', status=500).to_response()
    
@ideas_router.get('/{slug}', response={200: IdeaSchema, 404: ErrorResponse, 500: ErrorResponse})
def get_idea(request, slug: str) -> Response:
    try:
        idea: Idea = Idea.objects.get(slug=slug) 
        return IdeaSchema.from_orm(idea)
    
    except Idea.DoesNotExist:
        return Response('Idea not found', status=404).to_response()
    
    except Exception as e:
        return Response(f'An error occurred while retrieving the idea: {str(e)}', status=500).to_response()
    
@ideas_router.put('/{slug}', response={200: MessageResponse, 404: ErrorResponse, 500: ErrorResponse})
def update_idea(request, slug: str, data: CreateIdeaSchema) -> Response:
    try:
        idea: Idea = Idea.objects.get(slug=slug)
        for attr, value in data.dict().items():
            setattr(idea, attr, value)  
        idea.save()  
        
        return Response('Idea updated successfully', status=200, data={"id": idea.id, "name":idea.name, "slug": idea.slug, "atualizado_em": idea.updated_at}).to_response()
    
    except Idea.DoesNotExist:
        return Response('Idea not found', status=404).to_response()
    
    except Exception as e:
        return Response(f'An error occurred while updating the idea: {str(e)}', status=500).to_response()

    
@ideas_router.put('/{slug}/rate', response={200: MessageResponse, 404: ErrorResponse, 500: ErrorResponse})
def rate_idea(request, slug: str, rate: str) -> Response:
    try:
        idea: Idea = Idea.objects.get(slug=slug)
        
        if rate == 'genius':
            idea.num_genius += 1
        elif rate == 'stupid':
            idea.num_stupid += 1
        else:
            return Response('Invalid rate', status=400).to_response()
        idea.save()
        
        return Response('Rating successfully', status=200).to_response()
    
    except Idea.DoesNotExist:
        return Response('Idea not found', status=404).to_response()
    
    except Exception as e:
        return Response(f'An error occurred while rating the idea: {str(e)}', status=500).to_response()

@ideas_router.put('/{slug}/unrate', response={200: MessageResponse, 404: ErrorResponse, 500: ErrorResponse})
def unrate_idea(request, slug: str, rate: str) -> Response:
    try:
        idea: Idea = Idea.objects.get(slug=slug)
        
        if rate == 'genius':
            idea.num_genius = max(0, idea.num_genius - 1)
            
        elif rate == 'stupid':
            idea.num_stupid = max(0, idea.num_stupid - 1)
            
        else:
            return Response('Invalid rate', status=400).to_response()
        
        idea.save()
        
        return Response('Unrating successfully', status=200).to_response()
    
    except Idea.DoesNotExist:
        return Response('Idea not found', status=404).to_response()
    
    except Exception as e:
        return Response(f'An error occurred while unrating the idea: {str(e)}', status=500).to_response()

@ideas_router.delete('/{slug}', response={204: MessageResponse, 404: ErrorResponse, 500: ErrorResponse})
def delete_idea(request, slug: str) -> Response:
    try:
        idea: Idea = Idea.objects.get(slug=slug)
        idea.delete()
        return Response('Idea deleted successfully', status=204).to_response()
    
    except Idea.DoesNotExist:
        return Response('Idea not found', status=404).to_response()
    
    except Exception as e:
        return Response(f'An error occurred while deleting the idea: {str(e)}', status=500).to_response()