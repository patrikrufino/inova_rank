from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from inova_rank_api.routers import auth, categories, ideas, users

app = FastAPI()

# CORS stands for Cross-Origin Resource Sharing.
# This is a list of origins that are allowed to make requests to the API.
origins = [
    'http://localhost',
    'http://localhost:8000',
    'http://localhost:3000',
]

# This is a security feature to prevent unauthorized access to the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(ideas.router)
app.include_router(categories.router)
