import datetime as DT

def uniform_date_string(date_str):
    if (date_str == "" or date_str == " "):
        return "NULL"
    
    date_str = date_str.replace('*', '')
    date_str = date_str.replace(',', '')
    date_str = date_str.replace(u'\xa0', ' ')
    date_str = date_str.replace(';', '')

    if (date_str[0] == ' '):
        date_str = date_str[1:]

    if ("vari" in date_str.lower() or len(date_str) == 0 or date_str == '' or date_str == "None"):
        return "NULL"
    elif ("jan" in date_str.lower()):
        return find_year(date_str, "-01-01")
    elif ("feb" in date_str.lower()):
        return find_year(date_str, "-02-02")
    elif ("mar" in date_str.lower()):
        return find_year(date_str, '-03-03')
    elif ("apr" in date_str.lower()):
        return find_year(date_str, '-04-04')
    elif ("may" in date_str.lower()):
        return find_year(date_str, '-05-05')
    elif ("jun" in date_str.lower()):
        return find_year(date_str, '-06-06')
    elif ("jul" in date_str.lower()):
        return find_year(date_str, '-07-07')
    elif ("aug" in date_str.lower()):
        return find_year(date_str, '-08-08')
    elif ("sep" in date_str.lower()):
        return find_year(date_str, '-09-09')
    elif ("oct" in date_str.lower()):
        return find_year(date_str, '-10-10')
    elif ("nov" in date_str.lower()):
        return find_year(date_str, '-11-11')
    elif ("dec" in date_str.lower()):
        return find_year(date_str, '-12-12')
    elif (len(date_str) == 7):
        date_str = DT.datetime.strptime(date_str, '%m/%d/%y')
        date_str = DT.datetime.strftime(date_str, '%Y-%m-%d')
        return date_str
    elif ((len(date_str) == 9 or len(date_str) == 8)):
        date_str = DT.datetime.strptime(date_str, '%m/%d/%Y')
        date_str = DT.datetime.strftime(date_str, '%Y-%m-%d')
    elif (len(date_str) == 10 and '/' in date_str):
        date_str = DT.datetime.strptime(date_str, '%m/%d/%Y')
        date_str = DT.datetime.strftime(date_str, '%Y-%m-%d')
        return date_str
    elif (len(date_str) == 10 and '-' in date_str):
        date_str = DT.datetime.strptime(date_str, '%Y-%m-%d')
        date_str = DT.datetime.strftime(date_str, '%Y-%m-%d')
        return date_str
    elif ("starting" in date_str.lower()):
        date_str = date_str.split(' ')[-1]
        date_str = DT.datetime.strptime(date_str, '%m/%d/%y')
        date_str = DT.datetime.strftime(date_str, '%Y-%m-%d')
        return date_str
    else:
        date_arr = date_str.split(' ')
        date_str = DT.datetime.strptime(date_arr[0], '%m/%d/%y')
        date_str = DT.datetime.strftime(date_str, '%Y-%m-%d')
        return date_str

def find_year(date_str, month):
    date_str = date_str.split(' ')[-1] + month
    date_str = DT.datetime.strptime(date_str, '%Y-%m-%d')
    date_str = DT.datetime.strftime(date_str, '%Y-%m-%d')
    return date_str