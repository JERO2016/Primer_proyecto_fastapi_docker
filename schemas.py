from pydantic import BaseModel
from datetime import datetime
from typing import Optional  # se agrega esta línea


class PostBase(BaseModel):
    content: str
    title: str

    class Config:
        orm_mode = True


class CreatePost(PostBase):
    class Config:
        orm_mode = True
        
class AuthorBase(BaseModel):
    nombre: str
    apodo: str

class AuthorCreate(AuthorBase):
    fecha_registro: Optional[datetime] = None
    
    class Config:
        orm_mode = True