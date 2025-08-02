"""
2023-07-01 create products table
"""
from alembic import op
import sqlalchemy as sa

revision = '20230701_create_products_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('sku', sa.String(64), nullable=False, unique=True, index=True),
        sa.Column('quantity', sa.Integer, nullable=False, server_default='0'),
        sa.Column('last_updated', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
    )
    op.create_index('ix_products_sku', 'products', ['sku'], unique=True)
    op.create_index('ix_products_name', 'products', ['name'])

def downgrade():
    op.drop_index('ix_products_name', table_name='products')
    op.drop_index('ix_products_sku', table_name='products')
    op.drop_table('products')
