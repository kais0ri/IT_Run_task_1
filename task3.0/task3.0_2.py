students = int(input('Please enter the number of the students: '))
apples = int(input('Please enter the number of apples: '))
division = apples/students
division = round(division)

print(f"Each student will get {division} apples.")

if apples % students != 0:
    print(f"There are {apples%students} apple(s) left.")

