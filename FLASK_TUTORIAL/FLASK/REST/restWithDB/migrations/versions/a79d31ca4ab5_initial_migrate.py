"""initial Migrate

Revision ID: a79d31ca4ab5
Revises: 
Create Date: 2021-02-25 00:12:36.428522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a79d31ca4ab5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee_details',
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_details')
    # ### end Alembic commands ###
