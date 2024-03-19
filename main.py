from fastapi import FastAPI
from app.routes import actors
from app.routes import defendant

app = FastAPI()

app.include_router(actors.router, tags=["actors"], prefix="/actors")
app.include_router(defendant.router, tags=["defendants"], prefix="/defendants")
