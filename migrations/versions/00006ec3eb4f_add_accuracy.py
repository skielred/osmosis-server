"""add accuracy

Revision ID: 00006ec3eb4f
Revises: 93012ce9a92f
Create Date: 2019-12-11 23:26:55.176914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00006ec3eb4f'
down_revision = '93012ce9a92f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('accuracy', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('score', 'accuracy')
    # ### end Alembic commands ###
