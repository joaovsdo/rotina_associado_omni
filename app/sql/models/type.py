import sqlalchemy as sa
import sqlalchemy.orm as orm

from models.model_base import ModelBase
from models.reason import Reason

from typing import List


types_reasons = sa.Table(
    'types_reasons',
    ModelBase.metadata,
    sa.Column('type_id', sa.Integer, sa.ForeignKey('types.id')),
    sa.Column('reason_id', sa.Integer, sa.ForeignKey('reasons.id'))
)


class Type(ModelBase):
    __tablename__: str = 'types'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(100), unique=True, nullable=False)

    reasons: List[Reason] = orm.relationship('Reason', secondary=types_reasons, backref='type_reason', lazy='joined')

