import asyncio

from sanic.response import json

from app.forms import StudentSchema
from app.domain.student import get_student, create_or_update_student


d = {'first_name': 'update-201', 'last_name': 'update-200', 'id_student_book': 1111196}
#d1 = {'first_name': 'save234534', 'last_name': 'asdfasf', 'id_student_book': 54562}
#d2 = {'first_name': 'save3457457', 'last_name': 'asdfasf', 'id_student_book': 6333}


class StudentResource:

    async def post(self, request, data):
        #data = {} if not request.json else request.json.copy()
        #data = StudentSchema().dump(data)
        created_student = await create_or_update_student(data=data)
        return created_student

    async def get(self, request, student_id):
        student = await get_student(student_id)
        print(student)
        return student

    async def put(self, request):

        pass

    async def delete(self, request):
        pass


stud = StudentResource()
loop = asyncio.get_event_loop()
loop.run_until_complete(stud.post('req', d))
loop.close()
