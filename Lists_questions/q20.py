# occurence of each element in the list and print the element with highes occurence

my_list = [5,1,"Shijo",56.32,5,5,"Math",1,1,"Math"]

result = []

for num in my_list:
    if num not in result:
        result.append(num)

highest_occurence_element = 0
highest_occurence = 0

for num in result:
    c = my_list.count(num)
    print(f"The number {num} occurs {c} times!")
    if c > highest_occurence:
        highest_occurence = c
        highest_occurence_element = num

print(f"Highest occurence element is {highest_occurence_element} which occurs {highest_occurence} times!")
