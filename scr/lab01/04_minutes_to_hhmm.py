minutes_input = int(input('Количество минут:'))
hour = 60
hours = minutes_input//hour
minutes = minutes_input-(hours*hour)
print(f'{hours}:{minutes:02d}')