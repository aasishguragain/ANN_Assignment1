def min_max_scale(data):
  if not data:
    return []
  min_val = min(data)
  max_val = max(data)
  if min_val == max_val:
    return [0.0] * len(data)
  scaled_data = [(x - min_val) / (max_val - min_val) for x in data]
  return scaled_data

first_data = [2, 3, 4, 5]
scaled_data1 = min_max_scale(first_data)
print(scaled_data1)

second_data = [10, 20, 30]
scaled_data2 = min_max_scale(second_data)
print(scaled_data2)

third_data = [-1, 0, 1]
scaled_data3 = min_max_scale(third_data)
print(scaled_data3)

data4 = [7, 7, 7, 7]
scaled_data4 = min_max_scale(data4)
print(scaled_data4)

data5 = [4,18,3,2,6]
scaled_data5 = min_max_scale(data5)
print(scaled_data5)