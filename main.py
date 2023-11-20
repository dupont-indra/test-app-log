from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print(f'Returning Hello World')
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print(f'Item ID : {item_id} and q : {q}')
    return {"item_id": item_id, "q": q}
