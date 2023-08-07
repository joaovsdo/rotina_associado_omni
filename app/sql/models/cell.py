import sqlalchemy as sa

from models.model_base import ModelBase


class Cell(ModelBase):
    __tablename__: str = 'cells'

    id:int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    name:str = sa.Column(sa.String(100), unique=True, nullable=False)

