from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase
import sqlalchemy.ext.declarative as dec

__engine = None


class SqlAlchemyBase(DeclarativeBase):
    pass


def global_init(db_conn_str):
    global __engine

    if __engine:
        return

    if not db_conn_str.strip():
        raise ValueError("Необходимо указать файл базы данных.")

    print(f"Подключение к базе данных")

    __engine = create_engine(db_conn_str, echo=False)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(__engine)


def create_session() -> Session:
    return Session(__engine)
