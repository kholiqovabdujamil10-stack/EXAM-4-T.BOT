from connection import connection_db


async def created_vacansy(position, salary, description):
    conn = await connection_db()
    try:
        await conn.execute("""
            INSERT INTO vacancies  (position, salary, description)
            VALUES ($1, $2)
        """, position, salary, description)
        return True
    except Exception as erorr:
        print(f"Create user error: {erorr}")

    finally:
        await conn.close()


async def get_vacancy():
    conn = await connection_db()
    try:
        return await conn.fetchrow("SELECT * FROM vacancies")
    except Exception as erorr:
        print(f"Get user error: {erorr}")
    finally:
        await conn.close()


async def check_admin():
    conn = await connection_db()
    try:
        return await conn.fetch("SELECT is_admin FROM vacancies")
    except Exception as erorr:
        print(f"Check admin error: {erorr}")

    finally:
        await conn.close()


async def get_employers():
    conn = await connection_db()
    try:
        return await conn.fetch("SELECT * FROM employers ORDER BY id")
    except Exception as erorr:
        print(f"Get categories error: {erorr}")

    finally:
        await conn.close()


async def get_applications(application_id):
    conn = await connection_db()
    try:
        return await conn.fetchrow(
            "SELECT * FROM applications WHERE id = $1", application_id
        )
    except Exception as erorr:
        print(f"Get category error: {erorr}")
    finally:
        await conn.close()



async def add_vacancy(position, salary, description, photo_file_id):
    conn = await connection_db()
    try:
        await conn.execute("""
            INSERT INTO vacancies (position, salary, description, photo_file_id)
            VALUES ($1, $2, $3, $4)
        """, position, salary, description, photo_file_id)
        return True
    except Exception as erorr:
        print(f"Add vacancy error: {erorr}")

    finally:
        await conn.close()


async def update_vacancy(vacancy_id, field, value):
    conn = await connection_db()
    try:
        result = await conn.execute(
            f"UPDATE vacancy SET = $1 WHERE id = $2", value, vacancy_id
        )
        return result == "UPDATE 1"
    except Exception as erorr:
        print(f"Update vacancy error: {erorr}")

    finally:
        await conn.close()



async def delete_vacancy(vacancy_id):
    conn = await connection_db()
    try:
        result = await conn.execute("DELETE FROM vacancies WHERE id = $1", vacancy_id)
        return result == "DELETE 1"
    
    except Exception as erorr:
        print(f"Delete vacancy_id error: {erorr}")

    finally:
        await conn.close()