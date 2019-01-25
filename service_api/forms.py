from marshmallow import Schema, ValidationError, fields, validates


class StudentSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    id_student_book = fields.Integer(required=True)

    @validates('email')
    def validate_email(self, value):
        print(value)
        if len(value) < 7:
            raise ValidationError('Length email must be more than 7')
        if len(value) > 30:
            raise ValidationError('Length email must not be more than 30')


class SubjectSchema(Schema):
    name = fields.String(required=True)


class QuestionSchema(Schema):
    text_question = fields.String(required=True)
    subject_id = fields.Integer(required=True)


class AnswerSchema(Schema):
    text_answer = fields.String(required=True)
    true_or_false_answer = fields.Boolean(required=True)
