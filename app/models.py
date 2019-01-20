from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Boolean, ForeignKey


metadata = MetaData()


association_table = Table(
    'subject_student_table',
    metadata,
    Column('student_id', Integer, ForeignKey('student.id')),
    Column('subject_id', Integer, ForeignKey('subject.id')),
)


student = Table(
    'student',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('id_student_book', Integer, nullable=False, unique=True),
)

subject = Table(
    'subject',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False)
)


question = Table(
    'question',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text_question', Text, nullable=False),
    Column('subject_id', Integer, ForeignKey('subject_id'))
)


answer = Table(
    'answer',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text_answer', String, nullable=True),
    Column('true_and_false_answer', Boolean, default=False),
    Column('question_id', Integer, ForeignKey('question.id'))
)