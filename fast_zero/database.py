from typing import Any, Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from fast_zero.settings import Settings

engine: Engine = create_engine(Settings().DATABASE_URL)


def get_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session
