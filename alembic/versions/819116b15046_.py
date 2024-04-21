"""empty message

Revision ID: 819116b15046
Revises: 0d089112d5d0
Create Date: 2024-04-07 23:49:48.412320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '819116b15046'
down_revision: Union[str, None] = '0d089112d5d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ejemplo', 'ide')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ejemplo', sa.Column('ide', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
