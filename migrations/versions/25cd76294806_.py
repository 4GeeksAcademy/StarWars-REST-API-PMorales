"""empty message

Revision ID: 25cd76294806
Revises: 79d6c9e282d7
Create Date: 2024-04-24 16:58:08.857610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25cd76294806'
down_revision = '79d6c9e282d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=250), nullable=True))

    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.drop_column('nombre')

    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###