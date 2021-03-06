"""empty message

Revision ID: c680666f05bb
Revises: 
Create Date: 2022-04-01 22:59:24.267036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c680666f05bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=16), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('sex', sa.String(length=2), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('insert_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
