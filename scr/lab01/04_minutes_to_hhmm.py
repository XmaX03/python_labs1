minutes_input = int(input('Минуты:'))
hour = 60
hours = minutes_input//hour
minutes = minutes_input-(hours*hour)
print(str(hours) + ':' + str(minutes))