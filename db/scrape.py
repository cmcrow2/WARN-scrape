import os
from state_data.tx import get_tx_data
from state_data.ca import get_ca_data
from state_data.ny import get_ny_data
from insert import insert_to_db
from dotenv import load_dotenv
load_dotenv()  

def download_csv():
    path = os.getenv('CSV_PATH')
    warn_scraper = os.getenv('WARN_SCRAPER_PATH')
    print(warn_scraper)

    os.system(f"{warn_scraper} --data-dir {path} tx")
    os.system(f"{warn_scraper} --data-dir {path} ca")
    os.system(f"{warn_scraper} --data-dir {path} ny")

    tx_data = get_tx_data()
    insert_to_db(tx_data)

    ca_data = get_ca_data()
    insert_to_db(ca_data)

    ny_data = get_ny_data()
    insert_to_db(ny_data)
