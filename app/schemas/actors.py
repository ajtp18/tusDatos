from pydantic import BaseModel

class ActorCreate(BaseModel):
    number: int
    date: str
    process_number: str
    action_infraction: str
    detail: str

class Actor(BaseModel):
    id: int
    number: int
    date: str
    process_number: str
    action_infraction: str
    detail: str

    class Config:
        orm_mode = True