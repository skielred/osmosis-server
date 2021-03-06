"""add chart ssr and fk set_id

Revision ID: cf43cabe7ac2
Revises: 0e99fccad3b0
Create Date: 2019-12-18 02:22:50.529129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf43cabe7ac2'
down_revision = '0e99fccad3b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ssr', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_set_id', 'set', ['set_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chart', schema=None) as batch_op:
        batch_op.drop_column('ssr')
        batch_op.drop_constraint('fk_set_id', type_='foreignkey')

    # ### end Alembic commands ###
