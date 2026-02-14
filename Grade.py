nums = int(input("Enter the marks: "))

grade_dict = {
    'A+': 90,
    'A': 80,
    'B': 70,
    'C': 60,
    'D': 50,
    'F': 0
}

for grade in grade_dict:
    if nums >= grade_dict[grade]:
        print(grade)
        break