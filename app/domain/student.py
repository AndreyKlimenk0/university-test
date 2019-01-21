import asyncio
from typing import Dict

from app.models import Student
from app.database import get_engine

from sqlalchemy.exc import IntegrityError
from sqlalchemy import literal_column


async def create_or_update_student(data: Dict) -> dict:
    engine = await get_engine()
    async with engine.aqcuire() as connect:
        student = Student.insert().returning(literal_column('*')).values(**data)
        try:
            async with connect.execute(student) as current:
                cur_student = await current.fetchone()
        except IntegrityError:
            cur_student = await update_student(engine, data)
        return cur_student


async def update_student(connect, data: Dict) -> dict:
    id_stud_book = data['id_student_book']
    async with connect.execute(
            Student.update().where(
                Student.c.id_student_book == str(id_stud_book)).values(
                first_name=data['first_name'],
                last_name=data['last_name']
            )) as student:
        student = await student.fetchone()
    return student


async def get_student(student_id):
    engine = await get_engine()
    async with engine.acquire() as connect:
        async with connect.execute(
                Student.select().where(
                    Student.c.id == student_id
                )) as student:
            student = await student.fetchone()
    return student


async def update_student(data, student_id):
    #student_update = engine.exevute(Student.update().where(Student.c.id == student_id).value(**data))
    pass




# d = {'first_name': 'update-200', 'last_name': 'update-200', 'id_student_book': 56896}
# d1 = {'first_name': 'save234534', 'last_name': 'asdfasf', 'id_student_book': 54562}
# d2 = {'first_name': 'save3457457', 'last_name': 'asdfasf', 'id_student_book': 6333}
