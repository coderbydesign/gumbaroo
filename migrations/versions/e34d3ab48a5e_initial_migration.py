"""Initial Migration

Revision ID: e34d3ab48a5e
Revises: 
Create Date: 2021-11-30 09:09:23.567549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e34d3ab48a5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=True),
    sa.Column('gh_repo', sa.String(), nullable=True),
    sa.Column('gl_repo', sa.String(), nullable=True),
    sa.Column('deploy_file', sa.String(), nullable=True),
    sa.Column('namespace', sa.String(), nullable=True),
    sa.Column('branch', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('repo', sa.String(), nullable=False),
    sa.Column('ref', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('branch', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deploy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('ref', sa.String(), nullable=False),
    sa.Column('namespace', sa.String(), nullable=False),
    sa.Column('cluster', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deploy')
    op.drop_table('commit')
    op.drop_table('service')
    # ### end Alembic commands ###
