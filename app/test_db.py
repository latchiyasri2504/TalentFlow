import asyncio
from sqlalchemy import text
from app.database import engine

async def test():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
        print("DATABASE CONNECTION SUCCESS")
    await engine.dispose()

asyncio.run(test())