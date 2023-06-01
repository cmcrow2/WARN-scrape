import psycopg2
import os
from constants.state_list import state_list
from constants.queries import create_table, drop_table
from insert import insert_to_db
from dotenv import load_dotenv
load_dotenv()

# INSERT HERE: from state_data.scrape_{abbr} import get_{state}_data
from state_data.scrape_ak import get_alaska_data
from state_data.scrape_al import get_alabama_data
from state_data.scrape_az import get_arizona_data
from state_data.scrape_ca import get_california_data
from state_data.scrape_co import get_colorado_data
from state_data.scrape_ct import get_connecticut_data
from state_data.scrape_de import get_delaware_data
from state_data.scrape_fl import get_florida_data
from state_data.scrape_ga import get_georgia_data
from state_data.scrape_ia import get_iowa_data
from state_data.scrape_id import get_idaho_data
from state_data.scrape_il import get_illinois_data
from state_data.scrape_in import get_indiana_data
from state_data.scrape_ks import get_kansas_data
from state_data.scrape_ky import get_kentucky_data
from state_data.scrape_la import get_louisiana_data
from state_data.scrape_ma import get_massachusetts_data
from state_data.scrape_md import get_maryland_data
from state_data.scrape_me import get_maine_data
from state_data.scrape_mi import get_michigan_data
from state_data.scrape_mo import get_missouri_data
from state_data.scrape_ny import get_newyork_data
from state_data.scrape_oh import get_ohio_data
from state_data.scrape_pa import get_pennsylvania_data
from state_data.scrape_tn import get_tennessee_data
from state_data.scrape_tx import get_texas_data
from state_data.scrape_ut import get_utah_data
from state_data.scrape_mt import get_montana_data
from state_data.scrape_ne import get_nebraska_data
from state_data.scrape_nv import get_nevada_data

conn = psycopg2.connect(
   database=os.getenv('PG_DB'), user=os.getenv('PG_USER'), password=os.getenv('PG_PASS'), host='localhost', port= '5432'
)

cursor = conn.cursor()

cursor.execute("select version()")

for state in state_list:
    cursor.execute(drop_table(state))

    sql = create_table(state)
    cursor.execute(sql)

    print(f'Table "{state}" created successfully........')
    conn.commit()

conn.close()

# INSERT HERE: {abbr}_data = get_{state}_data()
print('\nScraping all state data........')
ak_data = get_alaska_data()
al_data = get_alabama_data()
az_data = get_arizona_data()
ca_data = get_california_data()
co_data = get_colorado_data()
ct_data = get_connecticut_data()
de_data = get_delaware_data()
fl_data = get_florida_data()
ga_data = get_georgia_data()
ia_data = get_iowa_data()
id_data = get_idaho_data()
il_data = get_illinois_data()
in_data = get_indiana_data()
ks_data = get_kansas_data()
ky_data = get_kentucky_data()
la_data = get_louisiana_data()
ma_data = get_massachusetts_data()
md_data = get_maryland_data()
me_data = get_maine_data()
mi_data = get_michigan_data()
ny_data = get_newyork_data()
oh_data = get_ohio_data()
pa_data = get_pennsylvania_data()
tn_data = get_tennessee_data()
tx_data = get_texas_data()
ut_data = get_utah_data()
mo_data = get_missouri_data()
mt_data = get_montana_data()
ne_data = get_nebraska_data()
nv_data = get_nevada_data()

# INSERT HERE: insert_to_db({abbr}_data, '{state}')
print('\nInserting all state data........')
insert_to_db(ak_data, 'alaska')
insert_to_db(al_data, 'alabama')
insert_to_db(az_data, 'arizona')
insert_to_db(ca_data, 'california')
insert_to_db(co_data, 'colorado')
insert_to_db(ct_data, 'connecticut')
insert_to_db(de_data, 'delaware')
insert_to_db(fl_data, 'florida')
insert_to_db(ga_data, 'georgia')
insert_to_db(ia_data, 'iowa')
insert_to_db(id_data, 'idaho')
insert_to_db(il_data, 'illinois')
insert_to_db(in_data, 'indiana')
insert_to_db(ks_data, 'kansas')
insert_to_db(ky_data, 'kentucky')
insert_to_db(la_data, 'louisiana')
insert_to_db(ma_data, 'massachusetts')
insert_to_db(md_data, 'maryland')
insert_to_db(me_data, 'maine')
insert_to_db(mi_data, 'michigan')
insert_to_db(ny_data, 'newyork')
insert_to_db(oh_data, 'ohio')
insert_to_db(pa_data, 'pennsylvania')
insert_to_db(tn_data, 'tennessee')
insert_to_db(tx_data, 'texas')
insert_to_db(ut_data, 'utah')
insert_to_db(mo_data, 'missouri')
insert_to_db(mt_data, 'montana')
insert_to_db(ne_data, 'nebraska')
insert_to_db(nv_data, 'nevada')
