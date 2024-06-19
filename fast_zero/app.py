from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root() -> Dict[str, str]:
    """
    Apenas para testar o servidor
    """
    return {'message': 'hello word'}
