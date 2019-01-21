from marshmallow import Schema, fields


class Student:
    def __init__(self, firs_name, last_name, id_student_book):
        self.first_name = firs_name
        self.last_name = last_name
        self.id_student_book = id_student_book


class StudentSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    id_student_book = fields.Integer(required=True)


class SubjectSchema(Schema):
    name = fields.String(required=True)


class QuestionSchema(Schema):
    text_question = fields.String(required=True)


class AnswerSchema(Schema):
    text_answer = fields.String(required=True)
    true_or_false_answer = fields.Boolean(required=True)

