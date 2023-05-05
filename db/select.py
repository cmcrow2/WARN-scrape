import psycopg2
import os
import datetime as DT
from dotenv import load_dotenv
load_dotenv()


def get_from_db():
    today = DT.datetime.now()
    delta = DT.timedelta(days = 7)
    week_ago = today - delta
    week_ago = DT.datetime.strftime(week_ago, '%Y-%m-%d')

    conn = psycopg2.connect(
    database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
    )

    cursor = conn.cursor()

    cursor.execute("select version()")

    sql =f'''SELECT * FROM state_data
    WHERE date_filed >= '{week_ago}'
    '''

    cursor.execute(sql)

    result = cursor.fetchall()

    print("Fetched Data........")
    conn.commit()

    conn.close()

    return result