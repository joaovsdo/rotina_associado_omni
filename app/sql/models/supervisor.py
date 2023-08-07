import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List

from models.model_base import ModelBase
from models.member import Member
from models.cell import Cell

members_supervisors = sa.Table(
    'members_supervisors',
    ModelBase.metadata,
    sa.Column('members_id', sa.Integer, sa.ForeignKey('members.id')),
    sa.Column('supervisors_id', sa.Integer, sa.ForeignKey('supervisors.id')),
)


class Supervisor(ModelBase):

    __tablename__: str = 'supervisors'

    id: int = sa.Column(sa.BigInteger, primary_key=True , autoincrement=True)
    name: str = sa.Column(sa.String(100), unique=True, nullable=False)

    cell_id: int = sa.Column(sa.Integer, sa.ForeignKey('cells.id'))
    cell: Cell = orm.relationship('Cell', lazy='joined')

    # List of members that pertence to a Supervisor
    members: List[Member] = orm.relationship('Member', secondary=members_supervisors, backref='member_supervisor', lazy='dynamic')
