from sanic.response import json


from service_api.resources import BaseResource
from service_api.forms import StudentSchema
from service_api.domain.student import get_student, create_student, update_student, delete_student


class StudentResource(BaseResource):

    async def post(self, request):
        data = {} if not request.json else request.json.copy()
        data, _ = StudentSchema(strict=True).load(data)
        student = await create_student(data=data)
        return json({**student}, status=200)

    async def get(self, request, student_id):
        student = await get_student(student_id)
        return json({**student})

    async def put(self, request):
        data = {} if not request.json else request.json.copy()
        data, _ = StudentSchema(strict=True).dump(data)
        student = await update_student(data=data)
        return json({**student})

    async def delete(self, request):
        data = {} if not request.json else request.json.copy()
        data, _ = StudentSchema(strict=True).dump(data)
        await delete_student(data=data)
        return json({'status': '200 ok'})
