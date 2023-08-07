import sqlalchemy as sa

from models.model_base import ModelBase


class Email(ModelBase):
    __tablename__: str = 'emails'

    id: int = sa.Column(sa.BigInteger , primary_key=True, autoincrement=True)
    email: str = sa.Column(sa.String(70), nullable=False, unique=True)
