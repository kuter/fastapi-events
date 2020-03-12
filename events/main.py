from typing import List

from fastapi import Depends, FastAPI

from sqlalchemy.orm import Session

import crud as events_crud
from database import SessionLocal
import schemas as events_schemas

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/events/", response_model=List[events_schemas.Event])
async def list(db: Session = Depends(get_db)):
    events = events_crud.get_events(db)
    return events


@app.post("/events/", response_model=events_schemas.Event)
async def create(
    event: events_schemas.EventCreate, db: Session = Depends(get_db)
):
    return events_crud.create_event(db=db, event=event)
