from fastapi import FastAPI
import models
from database import engine
import posts
from authors import router as authors_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
            
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(authors_router)