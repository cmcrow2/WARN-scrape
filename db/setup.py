import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

conn = psycopg2.connect(
   database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
)

cursor = conn.cursor()

cursor.execute("select version()")

# cursor.execute("DROP TABLE IF EXISTS WARN")

# sql ='''CREATE TABLE WARN(
#    STATE VARCHAR(255) NOT NULL,
#    CITY VARCHAR(255),
#    COUNTY VARCHAR(255),
#    COMPANY VARCHAR(255),
#    DATE_FILED DATE,
#    DATE_EFFECTIVE DATE,
#    EMPLOYEE_COUNT INT
# )'''

# cursor.execute(sql)
# print("Table created successfully........")
# conn.commit()

conn.close()
