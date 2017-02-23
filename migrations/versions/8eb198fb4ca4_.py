"""empty message

Revision ID: 8eb198fb4ca4
Revises: abd96d1f385e
Create Date: 2017-02-16 13:58:33.044302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eb198fb4ca4'
down_revision = 'abd96d1f385e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###