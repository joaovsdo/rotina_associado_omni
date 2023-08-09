import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import Optional, List

from models.email import Email
from models.model_base import ModelBase
from models.synergy import Synergy

import datetime

members_emails = sa.Table(
    'members_emails',
    ModelBase.metadata,
    sa.Column('member_id', sa.Integer, sa.ForeignKey('members.id')),
    sa.Column('email_id', sa.Integer, sa.ForeignKey('emails.id')),
)


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
    id_synergy: int = sa.Column(sa.Integer, sa.ForeignKey('synergies.id'))
    synergy: Optional[Synergy] = orm.relationship('Synergy', lazy='joined')

    email: List[Email] = orm.relationship('Email', secondary=members_emails, backref='member_email', lazy='dynamic')

