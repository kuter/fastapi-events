from sqlalchemy.orm import Session

import models as events_models
import schemas as events_schemas


def get_events(db: Session):
    return db.query(events_models.Event).all()


def create_event(db: Session, event: events_schemas.Event):
    db_event = events_models.Event(event=event.event)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
