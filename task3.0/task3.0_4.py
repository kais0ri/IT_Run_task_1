age = int(input('Please enter your age: '))

for i in range(0,age+1,2):
    if age % 2 == 0:
        print(i)
    elif age % 2 != 0:
        i += 1
        print(i)


