from sanic import Sanic
from sanic.response import json
from service_api.resources.resources_student import StudentResource
from service_api.resources.resources_subject import SubjectResources
from service_api.resources.resources_question import QuestionResources

app = Sanic()


async def test(request):
    return json({'status': '0k 222'})

app.add_route(SubjectResources.as_view(), '/subject')
app.add_route(StudentResource.as_view(), '/student/<student_id>')
app.add_route(StudentResource.as_view(), '/student')
app.add_route(QuestionResources.as_view(), '/question')
app.add_route(test, '/test')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
