"""empty message

Revision ID: f287582ae531
Revises: 3a07692f6c9f
Create Date: 2024-04-06 19:17:15.485811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'f287582ae531'
down_revision: Union[str, None] = '3a07692f6c9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ejemplo', sa.Column('ide', sa.Integer(), nullable=False))
    op.alter_column('ejemplo', 'id',
               existing_type=mysql.INTEGER(),
               comment=None,
               existing_comment='Primary Key',
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('ejemplo', 'create_time',
               existing_type=mysql.DATETIME(),
               nullable=False,
               comment=None,
               existing_comment='Create Time')
    op.alter_column('ejemplo', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ejemplo', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('ejemplo', 'create_time',
               existing_type=mysql.DATETIME(),
               nullable=True,
               comment='Create Time')
    op.alter_column('ejemplo', 'id',
               existing_type=mysql.INTEGER(),
               comment='Primary Key',
               existing_nullable=False,
               autoincrement=True)
    op.drop_column('ejemplo', 'ide')
    # ### end Alembic commands ###