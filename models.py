from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from datetime import datetime, timezone

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True)),
server_default = ('now()')

class Author(Base):
    __tablename__ = "authors"  # nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apodo = Column(String, unique=True, nullable=False)
    fecha_registro = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))