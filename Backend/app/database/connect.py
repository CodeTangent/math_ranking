import psycopg2


def get_connection():
    connection = psycopg2.connect(
        "postgresql://postgres:whatis_GARO4@db.jxtgbnrfiapnnqmckbbk.supabase.co:5432/postgres?sslmode=require"
    )
    return connection
