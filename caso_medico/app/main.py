from fastapi import FastAPI
from app.api.endpoints.queries import router

app = FastAPI()


app.include_router(router, prefix="/casos-medicos")
