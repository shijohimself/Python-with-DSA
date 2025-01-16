# bmi

b_wt = float(input("Enter your b weight: "))
b_ht = float(input("Enter your height: "))

bmi = b_wt / (b_ht ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("normal")
elif bmi >= 25 and bmi <= 29.9:
    print("overweight")
else:
    print("obese")
