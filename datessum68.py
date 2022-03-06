#
# sum day, month, decade and year
# return true if the sum is equal to 68
#
# TODO: check if it is a valid date
def sum68(d, m, y):
  decade, year = y // 100, y % 100
  result = False
  
  if d + m + decade + year == 68:
    result = True
  
  return result


print('Dates adding up to 68')
print('\tby Flávio Freitas, https://github.com/zz4fff\n')
for year in range(2022, 2023):
  for month in range(1, 13):
    for day in range(1, 32):
      if sum68(day, month, year):
        print(str(day) + '/' + str(month) + '/'+ str(year), end='; ')
print('\n')