import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List

from models.model_base import ModelBase
from models.cell import Cell

plataforms_cells = sa.Table(
    'plataforms_cells',
    ModelBase.metadata,
    sa.Column('plataform_id', sa.Integer, sa.ForeignKey('plataforms.id')),
    sa.Column('cell_id', sa.Integer, sa.ForeignKey('cells.id')),
)


class Plataform(ModelBase):

    __tablename__: str = 'plataforms'

    id: int = sa.Column(sa.BigInteger, primary_key=True , autoincrement=True)
    name: str = sa.Column(sa.String(100), unique=True, nullable=False)

    # List of members that pertence to a Supervisor
    members: List[Cell] = orm.relationship('Cell', secondary=plataforms_cells, backref='plataform_cell', lazy='dynamic')
