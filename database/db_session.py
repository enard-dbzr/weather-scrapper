import logging

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
        raise ValueError("You must specify db file")

    logging.info("Connecting to db...")
    __engine = create_engine(db_conn_str, echo=False)
    logging.info("Connected")

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(__engine)


def create_session() -> Session:
    return Session(__engine)
