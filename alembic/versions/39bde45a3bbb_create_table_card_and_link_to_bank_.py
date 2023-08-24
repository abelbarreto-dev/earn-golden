"""create table card and link to bank_accounts

Revision ID: 39bde45a3bbb
Revises: 5f7bc8445564
Create Date: 2023-08-23 13:44:42.307439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39bde45a3bbb'
down_revision: Union[str, None] = '5f7bc8445564'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('bank_account_id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('number', sa.String(length=128), nullable=False),
    sa.Column('due_date', sa.Date(), nullable=False),
    sa.Column('sec_code', sa.String(length=16), nullable=False),
    sa.Column('type_card', sa.Enum('credit', 'debit', 'prepaid'), nullable=False),
    sa.Column('balance', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['bank_account_id'], ['bank_accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    # ### end Alembic commands ###