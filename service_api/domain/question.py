from service_api.models import Question
from service_api.database import get_engine


async def get_question(question_id):
    pass


async def create_question(data):
    engine = await get_engine()
    async with engine.acquire() as connect:
        async with connect.execute(Question.insert().values(data)) as cur_question:
            question = await cur_question.fetchone()
    return question
