year = int(input('enter tha year'))
if (year % 4 == 0) and (year % 100 != 0):
  print('the given year {year } is leap year')
else:
  print(f'the given year {year}is not leap year ')
