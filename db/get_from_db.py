import psycopg2
import os
from dotenv import load_dotenv
from db.constants.queries import all_data_week
load_dotenv()


def get_from_db(state):
    conn = psycopg2.connect(
    database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
    )

    cursor = conn.cursor()

    cursor.execute("select version()")

    cursor.execute(all_data_week(state))

    result = cursor.fetchall()

    print("Fetched Data........")
    conn.commit()

    conn.close()

    return result