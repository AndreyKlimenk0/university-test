from aiopg.sa import create_engine, Engine


async def get_engine():
    result = await create_engine(user='andrey', password='andrey27', database='university_test', host='127.0.0.1')
    return result
