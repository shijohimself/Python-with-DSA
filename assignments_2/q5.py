# program to calculate bill

final_amount = int(input("Final maount: "))

if final_amount > 50000:
    discount = final_amount * 0.3
    amt_after_discount = final_amount - discount
    print(discount)
    print(amt_after_discount)
elif final_amount >= 40000 and final_amount <= 49999:
    discount = final_amount * 0.25
    amt_after_discount = final_amount - discount
    print(discount)
    print(amt_after_discount)
elif final_amount >= 30000 and  final_amount <= 39999:
    discount = final_amount * 0.2
    amt_after_discount = final_amount - discount
    print(discount)
    print(amt_after_discount)
elif final_amount >= 10000 and final_amount <= 29999:
    discount = final_amount * 0.1
    amt_after_discount = final_amount - discount
    print(discount)
    print(amt_after_discount) 
elif final_amount <= 9999:
    print("No discount")
else:
    print("Invalid!")