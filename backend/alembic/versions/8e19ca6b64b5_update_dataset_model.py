"""Update dataset model

Revision ID: 8e19ca6b64b5
Revises: eb489037bcef
Create Date: 2024-12-09 12:04:05.582563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8e19ca6b64b5'
down_revision: Union[str, None] = 'eb489037bcef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('datasets', 'data',
               existing_type=postgresql.BYTEA(),
               type_=sa.Text(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('datasets', 'data',
               existing_type=sa.Text(),
               type_=postgresql.BYTEA(),
               existing_nullable=False)
    # ### end Alembic commands ###
