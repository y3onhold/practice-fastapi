"""add content column to posts table

Revision ID: 58eda94ab98e
Revises: 725fccfbdda5
Create Date: 2024-10-09 15:56:08.199633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58eda94ab98e'
down_revision: Union[str, None] = '725fccfbdda5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
