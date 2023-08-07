import sqlalchemy as sa

from models.model_base import ModelBase


class Reason(ModelBase):
    __tablename__: str = 'reasons'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String, unique=True, nullable=False)

