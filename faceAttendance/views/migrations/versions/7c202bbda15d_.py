"""empty message

Revision ID: 7c202bbda15d
Revises: 
Create Date: 2023-10-13 23:36:34.657073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c202bbda15d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_question'))
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('image_path', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_student'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email'))
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name=op.f('fk_answer_question_id_question'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_answer'))
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.String(length=200), nullable=False),
    sa.Column('image_path', sa.String(length=255), nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['professor_id'], ['user.id'], name=op.f('fk_course_professor_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_course'))
    )
    op.create_table('attendance_check',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('check_week', sa.Integer(), nullable=False),
    sa.Column('result', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name=op.f('fk_attendance_check_course_id_course'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name=op.f('fk_attendance_check_student_id_student'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_attendance_check'))
    )
    op.create_table('course_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name=op.f('fk_course_student_course_id_course'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name=op.f('fk_course_student_student_id_student'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_course_student'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course_student')
    op.drop_table('attendance_check')
    op.drop_table('course')
    op.drop_table('answer')
    op.drop_table('user')
    op.drop_table('student')
    op.drop_table('question')
    # ### end Alembic commands ###
