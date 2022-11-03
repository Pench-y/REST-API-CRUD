from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import uuid4 as uuid

app = FastAPI()

#Storage
posts = []

#Post Model
class Post (BaseModel):
    id: Optional[str]
    name: str
    training: str
    experience: str
    number: str
    created_at: datetime = datetime.now()
    published_at: datetime 
#Route get
@app.get('/')
def read_root():
    return{"Welcome": "Welcome to my REST API"}
#Return data
@app.get('/posts')
def get_posts():
    return posts
#Create post
@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts [-1]
#Delete post
@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
        return {"message": "Post has been deleted succesfully"}
    return "Not found"
#Update post
@app.put('/posts{post_id}')
def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["name"] = updatePost.name
            posts[index]["trainig"] = updatePost.training
            posts[index]["experience"] = updatePost.experience
            posts[index]["number"] = updatePost.number
        return {"message": "Post has been update succesfully"}
    return "Not found"