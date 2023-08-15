"""empty message

Revision ID: 80bd5d2c97c5
Revises: 472eaa30cd5c
Create Date: 2023-08-15 00:22:32.141451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80bd5d2c97c5'
down_revision = '472eaa30cd5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('characters')
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('people_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('favorites_characters_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'people', ['people_id'], ['id'])
        batch_op.drop_column('characters_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('characters_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorites_characters_id_fkey', 'characters', ['characters_id'], ['id'])
        batch_op.drop_column('people_id')

    op.create_table('characters',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('birth_year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('eye_color', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('hair_color', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mass', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='characters_pkey')
    )
    op.drop_table('people')
    # ### end Alembic commands ###