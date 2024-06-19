### FastAPI: Construindo uma API do Zero

Este repositório contém materiais e instruções para começar a desenvolver uma API usando FastAPI. Abaixo estão os passos para configurar seu ambiente de desenvolvimento e executar seu primeiro "Hello, World!" com testes.

---

#### Configuração do Ambiente

Para começar, certifique-se de ter as seguintes ferramentas instaladas:

- Editor de texto de sua escolha (recomendado: GNU/Emacs)
- Terminal de sua escolha (recomendado: Terminator)
- Python 3.11+ instalado (recomendado via pyenv)
- Poetry para gerenciamento de pacotes
- Git para controle de versão
- Docker (opcional, mas recomendado para containerizar a aplicação)

#### Instalação do Python via Pyenv

Se necessário, use pyenv para instalar a versão adequada do Python:

```bash
pyenv install 3.12.3
pyenv global 3.12.3
```

#### Instalação do Poetry

Para instalar o Poetry, use pipx:

```bash
pipx install poetry
```

#### Criando e Configurando o Projeto FastAPI

Crie um novo projeto FastAPI com Poetry e navegue até o diretório criado:

```bash
poetry new nome_do_projeto
cd nome_do_projeto
```

Defina a versão do Python para o projeto e instale o FastAPI:

```bash
pyenv local 3.12.3
poetry add fastapi
```

#### Executando o Primeiro "Hello, World!" com FastAPI

Crie uma função básica para retornar "Hello, World!" em `app.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}
```

Ative o ambiente virtual do Poetry e execute o servidor FastAPI:

```bash
poetry shell
uvicorn nome_do_projeto.app:app --reload
```

Abra um navegador e visite [http://127.0.0.1:8000](http://127.0.0.1:8000) para ver a mensagem.

#### Instalando Ferramentas de Desenvolvimento

Instale ferramentas como pytest, taskipy e ruff para desenvolvimento:

```bash
poetry add --group dev pytest taskipy ruff
```

Configure as ferramentas no arquivo `pyproject.toml` conforme necessário para linting, formatação e execução de testes.

#### Executando Testes com Pytest

Crie um diretório `tests` e um arquivo `test_app.py` para testar a API:

```python
from fastapi.testclient import TestClient
from nome_do_projeto.app import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, World!'}
```

Execute os testes usando pytest:

```bash
pytest
```

---

Siga esses passos para configurar seu ambiente de desenvolvimento, criar uma API básica com FastAPI e começar a escrever testes para sua aplicação.