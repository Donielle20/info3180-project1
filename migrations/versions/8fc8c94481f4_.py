"""empty message

Revision ID: 8fc8c94481f4
Revises: 5a6c458adfcb
Create Date: 2023-03-09 18:38:53.337589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fc8c94481f4'
down_revision = '5a6c458adfcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.add_column(sa.Column('filename', sa.String(length=80), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.drop_column('filename')

    # ### end Alembic commands ###