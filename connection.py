import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

passw = os.getenv("PASSWORD_DB")


async def connection_db():
    return await asyncpg.connect(
        host="localhost",
        port=5432,
        user="postgres",
        database="lesson 1",
        password=passw
    )


async def create_table():
    try:
        conn = await connection_db()
        await conn.execute("""

            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                user_name TEXT,
                telegram_id BIGINT UNIQUE NOT NULL                        
            );
        
            CREATE TABLE IF NOT EXISTS employer (
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT UNIQUE NOT NULL,
                employer_name TEXT
            );

            CREATE TABLE IF NOT EXISTS vacancies (
                vacancies_id SERIAL PRIMARY KEY,
                employer_id int references employer(employer_id),
                position 
                salary bigint,
                description text,
                photo_file_id text,
                status text
                created_at TIMESTAMP DEFAULT NOW()
            );

            CREATE TABLE IF NOT EXISTS applications (
                applications_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id),
                vacancy_id INTEGER REFERENCES vacancies(vacancy_id),
                applied_at timestamp default now()
            );
        """)

        print("Database tables created successfully")

    except Exception as error:
        print(f"Database creation error: {error}")

    finally:
        await conn.close()