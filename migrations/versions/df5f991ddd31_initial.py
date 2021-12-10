"""Initial

Revision ID: df5f991ddd31
Revises: 
Create Date: 2021-12-07 16:12:01.330435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df5f991ddd31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Categories',
    sa.Column('CategoryID', sa.Integer(), nullable=False),
    sa.Column('CategoryName', sa.String(length=80), nullable=False),
    sa.Column('Description', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('CategoryID')
    )
    op.create_table('Products',
    sa.Column('ProductID', sa.Integer(), nullable=False),
    sa.Column('ProductName', sa.String(length=40), nullable=False),
    sa.Column('SupplierID', sa.Integer(), nullable=False),
    sa.Column('CategoryId', sa.Integer(), nullable=False),
    sa.Column('QuantityPerUnit', sa.String(length=20), nullable=False),
    sa.Column('UnitPrice', sa.Float(), nullable=False),
    sa.Column('UnitsInStock', sa.Integer(), nullable=False),
    sa.Column('UnitsOnOrder', sa.Integer(), nullable=False),
    sa.Column('ReorderLevel', sa.Integer(), nullable=False),
    sa.Column('Discontinued', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['CategoryId'], ['Categories.CategoryID'], ),
    sa.PrimaryKeyConstraint('ProductID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Products')
    op.drop_table('Categories')
    # ### end Alembic commands ###