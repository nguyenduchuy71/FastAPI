from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'duchuy'}}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/cmts')
def cmts(limit:int=2, published:bool=True,sort:Optional[str]=None):
    return {'limit cmts':limit,"pub":published}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def creat_blog(request:Blog):
    return {'data':f'Blog is created with {request.title}'}