from sanic.response import json

from service_api.resources import BaseResource
from service_api.forms import QuestionSchema
from service_api.domain.question import get_question, create_question


class QuestionResources(BaseResource):

    async def get(self, request, question_id):
        question = await get_question(question_id)
        return json({'question': question})

    async def post(self, request):
        print(request.json)
        data = {} if not request.json else request.json.copy()
        data, _ = QuestionSchema(strict=True).dump(data)
        print(data)
        created_question = await  create_question(data=data)
        return json({'created_question': created_question})

    async def put(self):
        pass

    async def delete(self):
        pass
