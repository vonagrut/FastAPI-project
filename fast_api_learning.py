from fastapi import FastAPI, Query
from schemas import Book
from typing import List


app = FastAPI()


# @app.get('/')
# def home():
#     return {"key": "some_text"}
#
#
# @app.get('/{pk}')
# def get_item(pk: int, q: str = None):
#     return {"key": pk, "q": q}
#
#
# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "item": item}


@app.post('/book')
def create_book(item: Book):
    return item


# (...) - Means that query is required
@app.get('/book')
def get_book(q: List[str] = Query(['text', 'text_2'], min_length=2, max_length=5, description='Write some text...', depricated=True)):
    return q