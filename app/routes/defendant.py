from app.provider.defendant_provider import DefendantProvider
from app.scrap.driver_init import init_chrome
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.defendant import Defendant
from database.base import get_db
from typing import List

router = APIRouter()

@router.get("/defendants", response_model=List)
def get_defendants(db: Session = Depends(get_db), cc_defendant: str = None):
    url = "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros"
    driver = init_chrome(url)
    defendant_provider = DefendantProvider(driver)
    defendants = defendant_provider.extract_actor_process(cc_defendant)
    driver.quit()
    return defendants

@router.get("/defendants-in-database", response_model=List)
def get_all_defendants(db: Session = Depends(get_db)):
    return db.query(Defendant).all()