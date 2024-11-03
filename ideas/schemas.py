from ninja import ModelSchema, Schema
from .models import Idea

class CreateIdeaSchema(ModelSchema):
  class Meta:
    model: Idea = Idea
    fields: list[str] = ['name', 'content']
class ListAllIdeasSchema(ModelSchema):
  class Meta:
    model: Idea = Idea
    fields: list[str] = ['id', 'name', 'slug', 'num_genius', 'num_stupid', 'created_at']
class IdeaSchema(ModelSchema):
    class Meta:
        model = Idea
        fields: list[str] = ['id', 'name', 'slug', 'content', 'num_genius', 'num_stupid', 'created_at', 'updated_at']
class UpdateIdeaSchema(ModelSchema):
    class Meta:
        model = Idea
        fields: list[str] = ['name', 'content']