from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root() -> Dict[str, str]:
    """
    Apenas para testar o servidor
    """
    return {'message': 'hello word'}


@app.get('/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello() -> str:
    """retornará hello world em html"""
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
