"""
start
end
total of all numbers
"""

start = int(input("Start = "))
end = int(input("end = "))
total = 0
for i in range(start, end + 1):
    total += i
print(total)