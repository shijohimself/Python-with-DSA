"""
keep on asking character from user
stop it until he/she press q

enter char - r
enter char - s
enter char - t
enter char - u
enter char - q

ans = rstu
"""

string = ""
while True:
    n = input("Enter char = ")
    if n != 'q':
        string += n
    else:
        break
print(string)

