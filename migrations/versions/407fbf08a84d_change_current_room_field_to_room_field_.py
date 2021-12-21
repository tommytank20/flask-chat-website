"""change current_room field to room field in Users table

Revision ID: 407fbf08a84d
Revises: 4d852f4aee1a
Create Date: 2021-12-21 21:19:23.013836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '407fbf08a84d'
down_revision = '4d852f4aee1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('room', sa.String(length=64), nullable=True))
    op.drop_column('user', 'current_room')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('current_room', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('user', 'room')
    # ### end Alembic commands ###