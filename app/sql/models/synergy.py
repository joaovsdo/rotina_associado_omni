import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List

from models.model_base import ModelBase
from models.cell import Cell

cells_synergies = sa.Table(
    'cells_synergies',
    ModelBase.metadata,
    sa.Column('id_synergy', sa.Integer, sa.ForeignKey('synergies.id')),
    sa.Column('id_cell', sa.Integer, sa.ForeignKey('cells.id'))
)


class Synergy(ModelBase):
    __tablename__: str = 'synergies'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

    synergys: List[Cell] = orm.relationship('Cell', secondary=cells_synergies, backref='cell', lazy='joined')

