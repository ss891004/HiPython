"""empty message

Revision ID: dd85961437ed
Revises: 
Create Date: 2022-03-03 23:29:15.016347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd85961437ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
