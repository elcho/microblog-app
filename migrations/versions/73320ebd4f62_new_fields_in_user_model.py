"""new fields in user model

Revision ID: 73320ebd4f62
Revises: fef8a5e9bd27
Create Date: 2018-03-28 14:41:04.098089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73320ebd4f62'
down_revision = 'fef8a5e9bd27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###