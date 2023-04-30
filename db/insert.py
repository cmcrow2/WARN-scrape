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
        if (row['date_filed'] == "NULL"): 
            date_filed = "NULL"
        else: 
            date_filed = f"TO_DATE('{row['date_filed']}','YYYY-MM-DD')"

        if (row['date_effective'] == "NULL"): 
            date_effective = "NULL"
        else: 
            date_effective = f"TO_DATE('{row['date_effective']}','YYYY-MM-DD')"

        values = f"""VALUES (
            '{row['state']}', 
            '{row['location']}', 
            '{row['company'].replace("'", "_")}',  
            {date_filed},
            {date_effective}, 
            '{row['employee_count']}')"""
        
        sql = f"""INSERT INTO state_data {col_names} {values}"""

        cursor.execute(sql)

        conn.commit()

    print("Data saved successfully........")
    conn.close()