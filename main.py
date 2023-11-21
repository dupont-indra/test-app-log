from typing import Union

from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
def read_root():
    logger.debug(f'This is a debug message ')
    print(f'This is a print hello world')
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logger.info(f'This is an info message , item : {item_id}')
    logger.error(f' This is an error message')
    return {"item_id": item_id, "q": q}
