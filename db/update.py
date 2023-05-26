import psycopg2
from db.constants.queries import update_values
from dotenv import load_dotenv
import os
load_dotenv()

def update_db(state):
    conn = psycopg2.connect(
        database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
    )

    cursor = conn.cursor()

    cursor.execute("select version()")

    sql = update_values(state)

    cursor.execute(sql)

    conn.commit()

    print(f"{state} data updated successfully........")
    conn.close()