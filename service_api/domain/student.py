from typing import Dict

from service_api.models import Student
from service_api.database import get_engine
from sqlalchemy import literal_column
from psycopg2 import IntegrityError


async def create_student(data: Dict) -> Dict:
    engine = await get_engine()
    async with engine.acquire() as connect:
        try:
            async with connect.execute(Student.insert().returning(literal_column('*')).values(data)) as cur_student:
                student = await cur_student.fetchone()
                return dict(student)
        except IntegrityError:
            return {'status': 'Student already is'}


async def update_student(data: Dict):
    engine = await get_engine()
    id_stud_book = data['id_student_book']
    async with engine.acquire() as connect:
        async with connect.execute(
                Student.update().returning(literal_column('*')).where(
                    Student.c.id_student_book == str(id_stud_book)).values(
                    # first_name=data['first_name'],
                    # last_name=data['last_name']
                    data
                )) as cur_student:
            student = await cur_student.fetchone()
            print('Cur', student)
            return student


async def get_student(student_id) -> Dict:
    engine = await get_engine()
    async with engine.acquire() as connect:
        async with connect.execute(
                Student.select().where(
                    Student.c.id == student_id
                )) as student:
            student = await student.fetchone()
    return dict(student)


async def delete_student(data: Dict):
    engine = await get_engine()
    async with engine.acquire() as connect:
        await connect.execute(
            Student.delete().where(
                Student.c.id_student_book == str(data['id_student_book'])
            ))
