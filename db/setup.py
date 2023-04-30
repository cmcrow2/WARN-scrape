import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

conn = psycopg2.connect(
   database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
)

cursor = conn.cursor()

cursor.execute("select version()")

cursor.execute("DROP TABLE IF EXISTS state_data")

sql ='''CREATE TABLE state_data(
   STATE VARCHAR(500) NOT NULL,
   LOCATION VARCHAR(500),
   COMPANY VARCHAR(500),
   DATE_FILED DATE,
   DATE_EFFECTIVE DATE,
   EMPLOYEE_COUNT INT
)'''

cursor.execute(sql)

print("Table created successfully........")
conn.commit()

conn.close()
