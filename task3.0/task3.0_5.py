weight = float(input('Please, enter your weight: '))

for i in range (1,16):
 moon_weight = weight * 0.165
 weight += 1
 moon_weight = round(moon_weight,2)
 print(f"{i} year - {moon_weight}")
