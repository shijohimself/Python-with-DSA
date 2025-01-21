"""
start
end

total of num div by 7
"""

start = int(input("Start = "))
end = int(input("end = "))
count = 0

for i in range(start, end + 1):
    if i % 7 == 0:
        count += i
print(count)