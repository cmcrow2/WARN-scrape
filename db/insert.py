import psycopg2
from constants.queries import insert_builder
from dotenv import load_dotenv
import os
load_dotenv()

def insert_to_db(data, state):
    conn = psycopg2.connect(
        database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
    )

    cursor = conn.cursor()

    cursor.execute("select version()")

    for row in data:
        sql = insert_builder(row, state)

        cursor.execute(sql)

        conn.commit()

    state = data[0]['state']
    print(f"{state} data saved successfully........")
    conn.close()