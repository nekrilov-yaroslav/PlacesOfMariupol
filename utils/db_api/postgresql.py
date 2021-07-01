from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE PRIMARY KEY
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, fullname, username, telegram_id):
        sql = "INSERT INTO Users (full_name, username, telegram_id) VALUES($1, $2, $3);"
        return await self.execute(sql, fullname, username, telegram_id, execute=True)

    async def select_users(self):
        sql = "SELECT telegram_id FROM Users;"
        return await self.execute(sql, fetch=True)

    async def select_pickup(self):
        sql = "SELECT * FROM places WHERE category LIKE '%самовивіз%';"
        return await self.execute(sql, fetch=True)

    async def select_hookah(self):
        sql = "SELECT * FROM places WHERE category LIKE '%кальян%';"
        return await self.execute(sql, fetch=True)

    async def select_alcohol(self):
        sql = "SELECT * FROM places WHERE category LIKE '%алкоголь%';"
        return await self.execute(sql, fetch=True)

    async def select_business_lunch(self):
        sql = "SELECT * FROM places WHERE category LIKE '%бізнес_ланч%';"
        return await self.execute(sql, fetch=True)

    async def select_coffee(self):
        sql = "SELECT * FROM places WHERE category LIKE '%кава%';"
        return await self.execute(sql, fetch=True)

    async def select_d_central(self):
        sql = "SELECT * FROM places WHERE district LIKE '%Central%';"
        return await self.execute(sql, fetch=True)

    async def select_d_seaside(self):
        sql = "SELECT * FROM places WHERE district LIKE '%Seaside%';"
        return await self.execute(sql, fetch=True)

    async def select_d_left_coast(self):
        sql = "SELECT * FROM places WHERE district LIKE '%Left Coast%';"
        return await self.execute(sql, fetch=True)
