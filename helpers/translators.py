def translate_state_data(data, company, date_posted, layoff_date, layoff_number, city):
  state_data = []

  for index in reversed(range(0, len(data[date_posted]))):
      temp_data = {}
      temp_data['company'] = data[company][index]

      if (type(data[date_posted][index]) == str):
         temp_data['date_posted'] = data[date_posted][index]
      else:
        temp_data['date_posted'] = data[date_posted][index].strftime('%m/%d/%Y')

      if (type(data[layoff_date][index]) == str):
         temp_data['layoff_date'] = data[layoff_date][index]
      else:
        temp_data['layoff_date'] = data[layoff_date][index].strftime('%m/%d/%Y')

      temp_data['layoff_number'] = data[layoff_number][index]
      temp_data['city'] = data[city][index]
      state_data.append(temp_data)

  return state_data