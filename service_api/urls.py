from service_api.resources.resources_student import StudentResource
from service_api.resources.resources_subject import SubjectResources
from service_api.resources.resources_question import QuestionResources


def load_url(app):
    app.add_route(SubjectResources.as_view(), '/subject/<subject_id>')
    app.add_route(SubjectResources.as_view(), '/subject/>')
    app.add_route(StudentResource.as_view(), '/student/<student_id>')
    app.add_route(StudentResource.as_view(), '/student')
    app.add_route(QuestionResources.as_view(), '/question')
    app.add_route(QuestionResources.as_view(), '/question/<question_id>')
