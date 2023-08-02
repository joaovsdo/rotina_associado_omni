import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from models.model_base import ModelBase

from config import (DB_USERNAME, DB_PASSWORD, 
                    DB_HOST, DB_PORT, DB_NAME)

__engine: Optional[Engine] = None


# Function that configure the db conection
def create_engine() -> Engine:

    global __engine

    if __engine:
        return
    else:
        conn_str = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


# Function that use the configuration in __engine to make a session in the db
def create_session() -> Session:

    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

    return session

# 
def create_table() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models
    ModelBase.metadata.create_all(__engine)

