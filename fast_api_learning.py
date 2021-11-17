from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut
from typing import List


app = FastAPI()


# @app.get('/')
# def home():
#     return {"key": "some_text"}


# @app.get('/{pk}')
# def get_item(pk: int, q: str = None):
#     return {"key": pk, "q": q}


# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "item": item}


# @app.post('/book')
# def create_book(item: Book, author: Author, quantity: int = Body(...)):
#     return {"item": item, "author": author, "quantity": quantity}


# # embed - used to include key ex. "author" to request body
# @app.post('/author')
# def create_author(author: Author = Body(..., embed=True)):
#     return {"author": author}


# # (...) - Means that query is required
# @app.get('/book')
# def get_book(q: List[str] = Query(['text', 'text_2'], min_length=2, max_length=5, description='Write some text...', depricated=True)):
#     return q


# # Path - used to validate path (url)
# # Query - used to validate query parameter
# @app.get('/book/{pk}')
# def get_single_book(pk: int = Path(..., gt=1, le=25), pages: int = Query(None, gt=10, le=500)):
#     return {"pk": pk, "pages": pages}


# response_model_exclude_unset - used to exclude (True/False) unset properties from request
# response_model_exclude/include = {} - used to exclude/include by name of properties
# item.dict() used to transform item to dict()
@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    return BookOut(item.dict(), id=3)