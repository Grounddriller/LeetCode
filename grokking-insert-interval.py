def insert_interval(existing_intervals, new_interval):
  result = []
  i = 0
  n = len(existing_intervals)
  
  while i < n and existing_intervals[i][1] < new_interval[0]:
    result.append(existing_intervals[i])
    i += 1
    
  while i < n and existing_intervals[i][0] <= new_interval[1]:
    new_interval[0] = min(new_interval[0], existing_intervals[i][0])
    new_interval[1] = max(new_interval[1], existing_intervals[i][1])
    i += 1
    
  result.append(new_interval)
  
  while i < n:
    result.append(existing_intervals[i])
    i += 1
    
  return result
