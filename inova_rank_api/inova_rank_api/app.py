from fastapi import FastAPI

from inova_rank_api.routers import auth, categories, ideas, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(ideas.router)
app.include_router(categories.router)
