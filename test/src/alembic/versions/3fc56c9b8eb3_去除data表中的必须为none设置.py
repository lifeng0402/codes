"""去除data表中的必须为None设置

Revision ID: 3fc56c9b8eb3
Revises: ff76f737120e
Create Date: 2022-09-26 16:20:45.736051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc56c9b8eb3'
down_revision = 'ff76f737120e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
