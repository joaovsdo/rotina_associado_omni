import sqlalchemy as sa
import sqlalchemy.orm as orm

from sql.models.model_base import ModelBase
from sql.models.synergy import Synergy

import datetime


class Member(ModelBase):
    __tablename__: str = 'members'

    # Integer values
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    registration: int = sa.Column(sa.Integer, unique=True, nullable=False)
    phone_id: int = sa.Column(sa.Integer, unique=True, nullable=False)

    # BigInteger values
    name: str = sa.Column(sa.String(100), unique=False, nullable=False)
    name_id: str = sa.Column(sa.String(45), unique=True, nullable=False)

    entry_time: datetime = sa.Column(sa.Time, nullable=False)

    status: str = sa.Column(sa.String(30), unique=False, nullable=False, default='NF')
    action: str = sa.Column(sa.String(30), unique=False, nullable=False, default='NF')

    # ForeignKeys of Synergy and the maping of Synergy orm object for data manipulation in the querys from python
    id_synergy: int = sa.Column(sa.Integer, sa.ForeignKey('synergys.id'))
    synergy: Synergy = orm.relationship('Synergy', lazy='joined')

