
import asyncio

from app.database import engine, Base
from app import models


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    print("TalentFlow database tables created successfully!")


if __name__ == "__main__":
    asyncio.run(create_tables())
