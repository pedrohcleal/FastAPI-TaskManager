from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema
from pprint import pprint

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root() -> Dict[str, str]:
    """
    Apenas para testar o servidor
    """
    return {'message': 'hello word'}


@app.get('/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello() -> str:
    """retornará hello world em html"""
    return """<html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    pprint(database)
    return user
