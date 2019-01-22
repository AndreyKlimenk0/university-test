from service_api.app import app, test
from service_api.resources.student import StudentResource


def load_url(app_sanic):
    app_sanic.add_route(StudentResource.as_view(), "/student/<id:int>")
    app_sanic.add_route(test, '/test')
