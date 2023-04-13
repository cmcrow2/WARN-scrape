def filter_by_layoff_num(data, state):
  filtered_data = {
      state: []
  }

  for index in range(0, len(data[state])):
      if (data[state][index]['layoff_number'] >= 100):
          filtered_data[state].append(data[state][index])

  return filtered_data