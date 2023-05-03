import os
# from state_data.ak import get_ak_data
from state_data.tx import get_tx_data
from state_data.ca import get_ca_data
from state_data.ny import get_ny_data
from db.insert import insert_to_db

def download_csv():
    os.system("warn-scraper --data-dir /Users/camcrow/projects/WARN-scrape/exports tx")
    os.system("warn-scraper --data-dir /Users/camcrow/projects/WARN-scrape/exports ca")
    os.system("warn-scraper --data-dir /Users/camcrow/projects/WARN-scrape/exports ny")


    # ak_data = get_ak_data()
    # insert_to_db(ak_data)

    tx_data = get_tx_data()
    insert_to_db(tx_data)

    ca_data = get_ca_data()
    insert_to_db(ca_data)

    ny_data = get_ny_data()
    insert_to_db(ny_data)
