import psycopg2
import os
from insert import insert_to_db
from dotenv import load_dotenv
load_dotenv()

from state_data.scrape_tx import get_texas_data
from state_data.scrape_ca import get_california_data
from state_data.scrape_ny import get_newyork_data
from state_data.scrape_fl import get_florida_data
from state_data.scrape_pa import get_pennsylvania_data
from state_data.scrape_oh import get_ohio_data
from state_data.scrape_az import get_arizona_data
from state_data.scrape_ut import get_utah_data

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

tx_data = get_texas_data()
insert_to_db(tx_data)

ca_data = get_california_data()
insert_to_db(ca_data)

ny_data = get_newyork_data()
insert_to_db(ny_data)

fl_data = get_florida_data()
insert_to_db(fl_data)

pa_data = get_pennsylvania_data()
insert_to_db(pa_data)

oh_data = get_ohio_data()
insert_to_db(oh_data)

az_data = get_arizona_data()
insert_to_db(az_data)

ut_data = get_utah_data()
insert_to_db(ut_data)
