class_a = int(input('Please, enter the number of students in the class A: '))
class_b = int(input('Please, enter the number of students in the class B: '))
class_c = int(input('Please, enter the number of students in the class C: '))

class_a_division = class_a/2
class_b_division = class_b/2
class_c_division = class_c/2


class_a_remainder = (round((class_a/2)+(class_a%2)))-1
class_b_remainder = (round((class_b/2)+(class_b%2)))-1
class_c_remainder = (round((class_c/2)+(class_c%2)))-1


if class_a%2 == 0:
    print(f"There are {class_a} students in the class, so the they need {class_a_division} chairs.")
else:
    print(f"There are {class_a} students in the class, so the they need {class_a_remainder+1} chairs.")


if class_b%2 == 0:
    print(f"There are {class_b} students in the class, so the they need {class_b_division} chairs.")
else:
    print(f"There are {class_b} students in the class, so the they need {class_b_remainder+1} chairs.")


if class_c%2 == 0:
    print(f"There are {class_c} students in the class, so the they need {class_c_division}")
else:
    print(f"There are {class_c} students in the class, so the they need {class_c_remainder+1} chairs.")



