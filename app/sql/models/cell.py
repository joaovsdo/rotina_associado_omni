import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List

from models.model_base import ModelBase
from models.reason import Reason


cells_reasons = sa.Table(
    'cells_reasons', 
    ModelBase.metadata,
    sa.Column('cell_id', sa.Integer, sa.ForeignKey('cells.id')),
    sa.Column('reason_id', sa.Integer, sa.ForeignKey('reasons.id'))
)



class Cell(ModelBase):
    __tablename__: str = 'cells'

    id:int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    name:str = sa.Column(sa.String(100), unique=True, nullable=False)
    
    reason: List[Reason] = orm.relationship('Reason', secondary=cells_reasons, backref='cell_reason', lazy='dynamic')

