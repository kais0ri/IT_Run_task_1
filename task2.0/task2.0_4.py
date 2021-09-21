string = input('Please enter any line with capital and small letters: ')
x = 0
y = 0
count = len(string)
print('The length of the string is',count)
for i in string:
    if i.isupper():
        x = x + 1
        percent_capital = x / count *100
print('The percentage of the capital letters is',str(round(percent_capital,2))+'%')
    # elif i.islower():
    #     y = y + 1
    #     percent_lower = y / count * 100
    #     print('The percentage of the small letters is',round(percent_lower,3))
#     else:
#         percent_small = 100 - percent_capital
# print('The percentage of the small letters is',round(percent_small,3))

for i in string:
    if i.islower():
        y = y + 1
        percent_small = y / count *100
print('The percentage of the small letters is',str(round(percent_small,2))+'%')
    



