from app.provider.actor_provider import ActorProvider
from app.scrap.driver_init import init_chrome
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.actor import Actor
from database.base import get_db
from typing import List

router = APIRouter()

@router.get("/actors", response_model=List)
def get_actors(db: Session = Depends(get_db), cc_autor: str = None):
    url = "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros"
    driver = init_chrome(url)
    actor_provider = ActorProvider(driver)
    actors = actor_provider.extract_actor_process(cc_autor)
    driver.quit()
    return actors

@router.get("/actors-in-database", response_model=List)
def get_all_actors(db: Session = Depends(get_db)):
    return db.query(Actor).all()