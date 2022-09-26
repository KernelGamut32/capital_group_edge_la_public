import psycopg2
from psycopg2 import sql

connection = psycopg2.connect(
    host="localhost",
    database="psycopgtest",
    user="postgres",
    password="Password123",
)

connection.set_session(autocommit=True)

with connection.cursor() as cursor:
    cursor.execute('SELECT COUNT(*) FROM users')
    result = cursor.fetchone()
print(result)

def is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = %(username)s
        """, {
            'username': username
        })
        result = cursor.fetchone()

    if result is None:
        return False

    admin, = result
    return admin

def count_rows(table_name: str, limit: int) -> int:
    with connection.cursor() as cursor:
        stmt = sql.SQL("""
            SELECT
                count(*)
            FROM (
                SELECT
                    1
                FROM
                    {table_name}
                LIMIT
                    {limit}
            ) AS limit_query
        """).format(
            table_name = sql.Identifier(table_name),
            limit = sql.Literal(limit),
        )
        cursor.execute(stmt)
        result = cursor.fetchone()

    rowcount, = result
    return rowcount

print(is_admin('haki'))
print(is_admin('ran'))
print(is_admin('foo'))
print(is_admin("'; select true; --"))
print(is_admin('haki'))
print(is_admin("'; update users set admin = 'true' where username = 'haki'; select true; --"))
print(is_admin('haki'))

print(count_rows('users', 1))
print(count_rows('users', 10))
print(count_rows("(select 1) as foo; update users set admin = true where name = 'haki'; --", 1))