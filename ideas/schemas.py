from ninja import ModelSchema, Schema
from .models import Idea

class CreateIdeaSchema(ModelSchema):
  class Meta:
    model: Idea = Idea
    fields: list[str] = ['name', 'content']
    
class IdeaSchema(ModelSchema):
  class Meta:
    model: Idea = Idea
    fields: list[str] = ['id', 'name', 'content', 'num_genius', 'num_stupid', 'created_at', 'updated_at', 'status']