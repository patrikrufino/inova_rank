from ninja import NinjaAPI
from ideas.api import ideas_router

api = NinjaAPI()

api.add_router('ideas', ideas_router)
