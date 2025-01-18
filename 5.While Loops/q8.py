"""
start
end 
total of all even number
"""

st = int(input("Enter start num: "))
en = int(input("Enter end num: "))

i = st
j = en
count = 0
while i <= j:
    if i % 2 == 0:
        count += i
    i += 1
print(count)
