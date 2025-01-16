"""
18 above -> adult
13-17 -> teenager
below 13 -> child
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
elif age >= 13 and age <= 17:
    print("Teenager")
else:
    print("Child")