from fastapi import FastAPI

from inova_rank_api.routers import auth, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
