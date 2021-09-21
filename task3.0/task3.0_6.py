line = input('Please, enter your string: ')
print(line)
if line == line[::-1]:
    print('It is a palindrome!')
else:
    print("It's not a palindrome!")
