from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return {"key": "some_text"}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}