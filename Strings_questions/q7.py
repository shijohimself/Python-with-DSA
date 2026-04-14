# keep on asking char from user until he press q
mystr = ""

i = 0
while True:
    input_str = input("Enter ch = ")
    if input_str == 'q':
        mystr += input_str
        break
    else:
        mystr += input_str
print(mystr)


