from typing import Dict
from service_api.models import Subject
from service_api.database import get_engine
from sqlalchemy import literal_column


async def get_subject(subject_id: int) -> Dict:
    engine = await get_engine()
    async with engine.acquire() as connect:
        async with connect.execute(
                Subject.select().where(
                    Subject.c.id == str(subject_id)
                )) as cur_subject:
            subject = await cur_subject.fetchone()
        return subject


async def create_subject(data: Dict) -> Dict:
    engine = await get_engine()
    async with engine.acquire() as connect:
        async with connect.execute(
                Subject.insert().returning(literal_column('*')).values(
                    data
                )) as cur_subject:
            subject = await cur_subject.fetchone()
            return subject


async def delete_subject(subject_id):
    engine = await get_engine()
    async with engine.acquire() as connect:
        await connect.execute(
            Subject.delete().where(
                Subject.c.id == str(subject_id)
            ))