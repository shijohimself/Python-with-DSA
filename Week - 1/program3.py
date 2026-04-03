email = input("Enter your email: ")
password = input("Enter your password: ")
if email == "abc@gmail.com" and password == "abc123":
    print("Login Successful")
elif email == "abc@gmail.com" or password == "abc123":
    print("Password or email is incorrect! Login again.")
    password = input("Re-enter your password: ")
    if password == "abc123":
        print("Login Successful")
    else:
        print("Login Failed")
else:
    print("Login Failed")