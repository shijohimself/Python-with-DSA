# take 5 input and print avg
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
d = int(input("d : "))
e = int(input("e : "))

avg = (a + b + c + d + e) / 5
print(avg)

# print upto 2 decimals
print(f"Your answer is {avg:.2f}") # this can only be used in f-strings

print(round(avg,2))