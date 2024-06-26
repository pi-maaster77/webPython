"""empty message

Revision ID: 0d089112d5d0
Revises: f287582ae531
Create Date: 2024-04-06 19:25:58.107528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '0d089112d5d0'
down_revision: Union[str, None] = 'f287582ae531'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ejemplo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ide', sa.Integer(), nullable=False),
    sa.Column('create_time', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ejemplo')
    # ### end Alembic commands ###
