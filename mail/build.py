def send_no_data():
   html = '<html><head><style>'
   html += 'p {font-family: arial, sans-serif;font-size: 18px}'
   html += '</style></head><body>'
   html += f'<p>There is no new data available.</p></body></html>'

   return html

def build_html_table(data):
  table = f'<h2>WARN Notices:</h2>'
  table += '<table><tr>'
  table += '<th>State</th>'
  table += '<th>City/County</th>'
  table += '<th>Company</th>'
  table += '<th>Date Posted</th>'
  table += '<th>Date Layoffs Begin</th>'
  table += '<th>Number of Layoffs</th>'
  table += '</tr>'

  for i in range(len(data)):
      table += '<tr>'
      for j in range(len(data[i])):
        table += f'<td>{data[i][j]}</td>'
      table += '</tr>'
        
  table += '</table>'

  return table

def build_week_html(data):
  if (len(data) > 0):
      html = '<html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}'
      html += 'td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}'
      html += 'p {font-family: arial, sans-serif;font-size: 18px}'
      html += 'tr:nth-child(even) {background-color: #dddddd;}</style></head><body>'
      html += '<p>This is an auto-generated notification detailing'
      html += ' companies that have submitted WARN Notices last week.</p>'
      html += build_html_table(data)
      html += '</body></html>'
  else:
      html = send_no_data()

  return html
