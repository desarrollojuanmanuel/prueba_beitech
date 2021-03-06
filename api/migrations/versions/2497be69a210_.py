"""empty message

Revision ID: 2497be69a210
Revises: 25db5b662c75
Create Date: 2022-06-07 17:18:47.582681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2497be69a210'
down_revision = '25db5b662c75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=191), nullable=False),
    sa.Column('email', sa.String(length=191), nullable=False),
    sa.PrimaryKeyConstraint('customer_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###
