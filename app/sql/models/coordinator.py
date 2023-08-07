import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List

from models.model_base import ModelBase
from models.supervisor import Supervisor


coordinators_supervisors = sa.Table(
    'coordinators_supervisors',
    ModelBase.metadata,
    sa.Column('coordinator_id', sa.BigInteger, sa.ForeignKey('coordinators.id')),
    sa.Column('supervisors_id', sa.BigInteger, sa.ForeignKey('supervisors.id'))
)

class Coordinator(ModelBase):
    __tablename__: str = 'coordinators'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(100), nullable=False, unique=True)

    supervisors: List[Supervisor] = orm.relationship('Supervisor', secondary=coordinators_supervisors, backref='coordinator_supervisor', lazy='joined')

