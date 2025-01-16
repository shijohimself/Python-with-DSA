salary = int(input("Enter your salary: "))
if salary > 50000:
    increment = salary * 0.2
    salary += increment
    print(increment , "RANGE- I ")
    print(salary)
elif salary > 20000 and salary <= 50000:
    increment = salary * 0.15
    salary += increment
    print(increment, "RANGE- II")
    print(salary)
elif salary >= 10000 and salary <= 20000:
    increment = salary * 0.1
    salary += increment
    print(increment , "RANGE - III")
    print(salary)
elif salary < 10000:
    increment = salary * 0.05
    salary += increment
    print(increment, "RANGE - IV")
    print(salary)
else:
    print("invalid")