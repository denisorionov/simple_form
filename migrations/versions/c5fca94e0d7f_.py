"""empty message

Revision ID: c5fca94e0d7f
Revises: 
Create Date: 2021-09-05 17:20:28.273261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5fca94e0d7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('middle_name', sa.String(length=20), nullable=False),
    sa.Column('bornDate', sa.Date(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('user_profiles',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('education', sa.Text(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('citizenship', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    op.drop_table('user')
    # ### end Alembic commands ###
