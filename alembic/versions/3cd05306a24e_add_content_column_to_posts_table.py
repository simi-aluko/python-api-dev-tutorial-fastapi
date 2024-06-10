"""add content column to posts table

Revision ID: 3cd05306a24e
Revises: d918dea7b903
Create Date: 2024-06-08 21:02:45.452832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cd05306a24e'
down_revision: Union[str, None] = 'd918dea7b903'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
