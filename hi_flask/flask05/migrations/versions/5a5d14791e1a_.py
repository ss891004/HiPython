"""empty message

Revision ID: 5a5d14791e1a
Revises: 751e8b9f1d61
Create Date: 2022-02-10 23:53:31.330865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a5d14791e1a'
down_revision = '751e8b9f1d61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=11), nullable=True))
    op.add_column('user', sa.Column('insert_time', sa.DateTime(), nullable=True))
    op.create_unique_constraint(None, 'user', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'insert_time')
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###