"""alter due date to a custom format at card due date

Revision ID: b5fe6d31e918
Revises: 149dfd0f0146
Create Date: 2023-08-28 12:00:01.734469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.database.sqltypes import YearMonthDateDB


# revision identifiers, used by Alembic.
revision: str = 'b5fe6d31e918'
down_revision: Union[str, None] = '149dfd0f0146'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("cards", "due_date", type_=YearMonthDateDB(), nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("cards", "due_date", nullable=False, type_=sa.Date())
    # ### end Alembic commands ###
