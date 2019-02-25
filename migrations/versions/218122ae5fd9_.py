"""empty message

Revision ID: 218122ae5fd9
Revises: 388377d6adbf
Create Date: 2019-02-25 18:59:16.674211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218122ae5fd9'
down_revision = '388377d6adbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.add_column('compound', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'compound', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'compound', type_='foreignkey')
    op.drop_column('compound', 'category_id')
    op.drop_table('category')
    # ### end Alembic commands ###