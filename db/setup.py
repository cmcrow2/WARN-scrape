import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

conn = psycopg2.connect(
   database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
)

cursor = conn.cursor()

cursor.execute("select version()")

cursor.execute("DROP TABLE IF EXISTS WARN")

sql ='''CREATE TABLE WARN(
   STATE VARCHAR(500) NOT NULL,
   LOCATION VARCHAR(500),
   COMPANY VARCHAR(500),
   DATE_FILED VARCHAR(500),
   DATE_EFFECTIVE VARCHAR(500),
   EMPLOYEE_COUNT INT
)'''

print("Table created successfully........")
conn.commit()

conn.close()
