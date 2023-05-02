from state_data.scrape import download_csv
from state_data.ak import get_ak_data
from state_data.tx import get_tx_data
from state_data.ca import get_ca_data
from db.insert import insert_to_db

# download_csv()

ak_data = get_ak_data()
insert_to_db(ak_data)

tx_data = get_tx_data()
insert_to_db(tx_data)

ca_data = get_ca_data()
insert_to_db(ca_data)