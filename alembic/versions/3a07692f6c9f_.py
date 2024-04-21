"""empty message

Revision ID: 3a07692f6c9f
Revises: cd3d7253ebbc
Create Date: 2024-03-26 01:09:44.728885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '3a07692f6c9f'
down_revision: Union[str, None] = 'cd3d7253ebbc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hola')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hola',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False, comment='Primary Key'),
    sa.Column('create_time', mysql.DATETIME(), nullable=True, comment='Create Time'),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###