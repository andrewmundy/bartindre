"""empty message

Revision ID: 60c8899b4445
Revises: bde06cf6980d
Create Date: 2017-02-22 21:08:40.067976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c8899b4445'
down_revision = 'bde06cf6980d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drinks', sa.Column('img', sa.String(), nullable=True))
    op.add_column('drinks', sa.Column('instructions', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('drinks', 'instructions')
    op.drop_column('drinks', 'img')
    # ### end Alembic commands ###
