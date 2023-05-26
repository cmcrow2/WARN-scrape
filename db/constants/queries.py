import datetime as DT

today = DT.datetime.now()
delta = DT.timedelta(days = 7)
week_ago = today - delta
week_ago = DT.datetime.strftime(week_ago, '%Y-%m-%d')

def all_data_week(state):
    return f'''SELECT * FROM {state}
    WHERE STATUS = 'new'
    ORDER BY date_filed desc
    '''

def insert_builder(row, state):
    col_names = '(STATUS, ID, STATE, LOCATION, COMPANY, DATE_FILED, DATE_EFFECTIVE, EMPLOYEE_COUNT)'

    if (row['date_filed'] == "NULL" or row['date_filed'] == None): 
        date_filed = "NULL"
    else: 
        date_filed = f"TO_DATE('{row['date_filed']}','YYYY-MM-DD')"

    if (row['date_effective'] == "NULL") or row['date_effective'] == None: 
        date_effective = "NULL"
    else: 
        date_effective = f"TO_DATE('{row['date_effective']}','YYYY-MM-DD')"

    if (row['employee_count'] == 'NULL'):
        employee_count = 'NULL'
    else:
        employee_count = f"'{row['employee_count']}'"

    values = f"""VALUES (
        'new',
        '{row['id']}',
        '{row['state']}', 
        '{row['location']}', 
        '{row['company'].replace("'", "_")}',  
        {date_filed},
        {date_effective}, 
        {employee_count})"""
    
    sql = f"""INSERT INTO {state} {col_names} {values} ON CONFLICT (ID) DO NOTHING"""
    return sql

def create_table(state):
    return f'''CREATE TABLE {state}(
    STATUS VARCHAR(500) NOT NULL,
    ID INT PRIMARY KEY,
    STATE VARCHAR(500) NOT NULL,
    LOCATION VARCHAR(500),
    COMPANY VARCHAR(500),
    DATE_FILED DATE,
    DATE_EFFECTIVE DATE,
    EMPLOYEE_COUNT INT
    )'''

def drop_table(state):
    return f"DROP TABLE IF EXISTS {state}"

def update_values(state):
    return f'''UPDATE {state}
    SET STATUS = REPLACE(STATUS, 'new', 'seen')
    WHERE STATUS = 'new';'''