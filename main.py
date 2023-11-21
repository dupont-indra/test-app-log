from typing import Union

from fastapi import FastAPI
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
def read_root():
    logger.debug(f'Returing Hello World')
    print(f'This is a print hello world')
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logger.info(f'Info Log : {item_id}')
    logger.error(f'Error Log ')
    return {"item_id": item_id, "q": q}
