def translate_state_data(data):
  state_data = []
  temp_data = {}

  for index in reversed(range(0, len(data['NOTICE_DATE']))):
      temp_data['company'] = data['JOB_SITE_NAME'][index]
      temp_data['date_posted'] = data['NOTICE_DATE'][index].strftime('%m/%d/%y')
      temp_data['layoff_date'] = data['LayOff_Date'][index].strftime('%m/%d/%y')
      temp_data['layoff_number'] = data['TOTAL_LAYOFF_NUMBER'][index]
      temp_data['city'] = data['CITY_NAME'][index]
      state_data.append(temp_data)
      temp_data = {}

  return state_data