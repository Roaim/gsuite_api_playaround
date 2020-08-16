from .base_model import db, BaseModel


class Hello(BaseModel):
    name = db.Column(db.String(55))
    ip = db.Column(db.String(55))