def build_html_table(data, state):
  table = f'<h2>{state} WARN Notices:</h2>'
  table += '<table><tr>'
  table += '<th>Company</th>'
  table += '<th>City</th>'
  table += '<th>Date Posted</th>'
  table += '<th>Date Layoffs Begin</th>'
  table += '<th>Number of Layoffs</th>'
  table += '</tr>'

  for index in range(len(data[state])):
      temp_company = data[state][index]['company']
      temp_city = data[state][index]['city']
      temp_date_posted = data[state][index]['date_posted']
      temp_layoff_date = data[state][index]['layoff_date']
      temp_layoff_number = data[state][index]['layoff_number']
      
      table += '<tr>'
      table += f'<td>{temp_company}</td>'
      table += f'<td>{temp_city}</td>'
      table += f'<td>{temp_date_posted}</td>'
      table += f'<td>{temp_layoff_date}</td>'
      table += f'<td>{temp_layoff_number}</td>'
      table += '</tr>'

  table += '</table>'

  return table

def add_header(table, is_filtered):
  header = '<html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}'
  header += 'td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}'
  header += 'p {font-family: arial, sans-serif;font-size: 18px}'
  header += 'tr:nth-child(even) {background-color: #dddddd;}</style></head><body>'
  header += '<p>This is an auto-generated notification detailing companies that are planning to lay off'
  if (is_filtered):
     header += ' 100 or more'
  header += ' employees in 2023.</p>'
  header += table
  header += '</body></html>'

  return header