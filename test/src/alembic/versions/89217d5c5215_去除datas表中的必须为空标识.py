"""去除datas表中的必须为空标识

Revision ID: 89217d5c5215
Revises: 3fc56c9b8eb3
Create Date: 2022-09-26 16:21:47.117693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89217d5c5215'
down_revision = '3fc56c9b8eb3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('body', table_name='datas')
    op.drop_index('body_type', table_name='datas')
    op.drop_index('cookies', table_name='datas')
    op.drop_index('params', table_name='datas')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('params', 'datas', ['params'], unique=False)
    op.create_index('cookies', 'datas', ['cookies'], unique=False)
    op.create_index('body_type', 'datas', ['body_type'], unique=False)
    op.create_index('body', 'datas', ['body'], unique=False)
    # ### end Alembic commands ###
