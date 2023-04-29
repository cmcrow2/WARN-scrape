from state_data.scrape import download_csv
from state_data.ak import get_ak_data
from db.insert import insert_to_db

# download_csv()
ak_data = get_ak_data()
insert_to_db(ak_data)