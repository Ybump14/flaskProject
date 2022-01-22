"""empty message

Revision ID: 95878755079e
Revises: e81eb5467766
Create Date: 2022-01-22 19:41:42.726788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95878755079e'
down_revision = 'e81eb5467766'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed')
    # ### end Alembic commands ###
