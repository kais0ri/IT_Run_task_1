first_time = input('Enter the first time peroid like HH:MM:SS - ')
second_time = input('Enter the second time peroid like HH:MM:SS - ')
print(f"The first time period is {first_time}")
print(f"The second time period is {second_time}")

first_calc = int(first_time[0:2]) * 3600 + int(first_time[3:5]) * 60 + int(first_time[6:])
second_calc = int(second_time[0:2]) * 3600 + int(second_time[3:5]) * 60 + int(second_time[6:])

difference = second_calc  - first_calc
print(f"The difference in time periods is {difference} seconds")