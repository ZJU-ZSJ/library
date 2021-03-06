"""first init db

Revision ID: 812d1b9d5269
Revises: 
Create Date: 2018-04-06 07:00:37.323409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '812d1b9d5269'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cno', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('department', sa.String(length=64), nullable=True),
    sa.Column('type', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categorys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bno', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('press', sa.String(length=64), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categorys.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bno', sa.Integer(), nullable=True),
    sa.Column('cno', sa.Integer(), nullable=True),
    sa.Column('backornot', sa.Boolean(), nullable=True),
    sa.Column('btime', sa.DATETIME(), nullable=True),
    sa.Column('rtime', sa.DATETIME(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['bno'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('record')
    op.drop_table('book')
    op.drop_table('users')
    op.drop_table('categorys')
    op.drop_table('card')
    # ### end Alembic commands ###
