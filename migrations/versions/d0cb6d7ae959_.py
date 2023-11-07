"""empty message

Revision ID: d0cb6d7ae959
Revises: 5e642848dfc8
Create Date: 2023-11-07 11:23:12.820103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0cb6d7ae959'
down_revision = '5e642848dfc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('foto',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('foto',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
