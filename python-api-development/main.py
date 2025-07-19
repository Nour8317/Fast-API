from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
import time
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title:str
    content:str
    published:bool

@app.get("/")
async def root():
    return{"message":"success"}

@app.get("/posts")
async def get_posts():
    cursor.execute("SELECT * FROM posts")  
    posts = cursor.fetchall()              
    return {"data": posts}

@app.post("/createPost")
async def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title,content,published) values(%s, %s, %s) RETURNING * """,(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return{"Data":new_post}