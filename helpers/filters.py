import datetime as DT

def filter_by_layoff_num(data, state):
  filtered_data = {
      state: []
  }

  for index in range(0, len(data[state])):
      if (data[state][index]['layoff_number'] >= 100):
          filtered_data[state].append(data[state][index])

  return filtered_data

def filter_by_past_week(data, state):
  filtered_data = {
      state: []
  }

  today = DT.datetime.now()
  week_ago = today - DT.timedelta(days=7)
  week_ago = DT.datetime.strftime(week_ago, '%m/%d/%Y')
  week_ago = DT.datetime.strptime(week_ago, '%m/%d/%Y')

  for index in range(0, len(data[state])):
      temp_date = DT.datetime.strptime(data[state][index]['date_posted'], '%m/%d/%Y')

      if (temp_date >= week_ago):
         filtered_data[state].append(data[state][index])
  
  return filtered_data
