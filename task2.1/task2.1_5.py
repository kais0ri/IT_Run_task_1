numbers = [1,5,86,34,95,3,7,86,-32,-4]

max_number = max(numbers)
print(max_number)
min_number = min(numbers)
print(min_number)
min_index = numbers.index(min_number)
max_index = numbers.index(max_number)
numbers[min_index] = max_number
numbers[max_index] = min_number
print(numbers)