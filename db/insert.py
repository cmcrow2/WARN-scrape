import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

def insert_to_db(data):
    conn = psycopg2.connect(
    database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
    )

    cursor = conn.cursor()

    cursor.execute("select version()")

    col_names = '(STATE, LOCATION, COMPANY, DATE_FILED, DATE_EFFECTIVE, EMPLOYEE_COUNT)'
    for row in data:
        values = f"""VALUES (
            '{row['state']}', 
            '{row['location']}', 
            '{row['company'].replace("'", "_")}', 
            '{row['date_filed']}', 
            '{row['date_effective']}', 
            '{row['employee_count']}')"""
        
        sql = f"""INSERT INTO WARN {col_names} {values}"""

        cursor.execute(sql)

        conn.commit()

    print("Data saved successfully........")
    conn.close()