"""updated db

Revision ID: 42327b39d05c
Revises: 87e990d8ceab
Create Date: 2024-12-24 19:01:26.314700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42327b39d05c'
down_revision = '87e990d8ceab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('answer',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('answer',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=False)

    # ### end Alembic commands ###
