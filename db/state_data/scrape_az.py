import pandas as pd
import requests
import datetime as DT

def get_arizona_data():
    page = requests.get('https://www.azjobconnection.gov/search/warn_lookups?commit=Search&page=1&q%5Bemployer_name_cont%5D=&q%5Bmain_contact_contact_info_addresses_full_location_city_matches%5D=&q%5Bnotice_eq%5D=&q%5Bnotice_on_gteq%5D=2023-01-01&q%5Bnotice_on_lteq%5D=&q%5Bservice_delivery_area_id_eq%5D=&q%5Bzipcode_code_start%5D=')

    warn_data = pd.read_html(page.text)
    warn_data = warn_data[0].to_dict()

    arizona_db = []

    for idx in range(0, len(warn_data["Notice Date"])):
        temp_data = {}
        temp_data["state"] = "Arizona"
        temp_data["location"] = warn_data["ZIP"][idx]
        temp_data["company"] = warn_data["Employer"][idx]

        temp_data["date_filed"] = DT.datetime.strptime(warn_data["Notice Date"][idx], '%b %d, %Y')
        temp_data["date_filed"] = DT.datetime.strftime(temp_data["date_filed"], '%Y-%m-%d')

        temp_data["date_effective"] = "NULL"
        temp_data["employee_count"] = "NULL"

        arizona_db.append(temp_data)

    return arizona_db
