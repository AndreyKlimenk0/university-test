import asyncio
from aiopg.sa import create_engine, Engine


async def get_engine():
    result = await create_engine(user='andrey', password='andrey27', database='university_test', host='127.0.0.1')
    return result


async def test():
    engine = await get_engine()
    async with engine.acquire() as connect:
        async with connect.execute('SELECT * FROM student') as cur:
            r = await cur.fetchone()
            print(r)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())
# loop.close()