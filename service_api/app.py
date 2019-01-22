from sanic import Sanic
from sanic.response import json
from service_api.resources.student import StudentResource
from service_api.resources.subject import SubjectResources
from service_api.resources.question import QuestionResources

app = Sanic()


async def test(request):
    print(dir(request))
    print(request.json)
    return json({'status': '0k 222'})


if __name__ == '__main__':
    app.add_route(SubjectResources.as_view(), '/subject/<subject_id>')
    app.add_route(StudentResource.as_view(), '/student')
    app.add_route(QuestionResources.as_view(), '/question')
    app.add_route(test, '/test')
    app.run(host='127.0.0.1', port=8000)
