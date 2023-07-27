"""update case table flied

Revision ID: bff215a5f43f
Revises: c3c838d2ea7e
Create Date: 2023-07-27 19:17:36.182861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bff215a5f43f'
down_revision = 'c3c838d2ea7e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('case', sa.Column('extract', sa.JSON(), nullable=True))
    op.add_column('case', sa.Column('checkout', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('case', 'checkout')
    op.drop_column('case', 'extract')
    # ### end Alembic commands ###
