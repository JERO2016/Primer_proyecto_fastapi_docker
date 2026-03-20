from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Author
from schemas import AuthorCreate

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/", response_model=AuthorCreate)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author(nombre=author.nombre, apodo=author.apodo)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
