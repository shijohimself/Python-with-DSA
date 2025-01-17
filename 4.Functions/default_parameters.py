# default parameters
# required and optional parameters!
# order should be maintained!

def greet(first_name, last_name = "", age = 0):
    print(f"Hello {first_name} {last_name} your age is = {age}")
    print("Done")


def marks(sci = 0 , eng = 0 , hin = 0 , sst = 0 , comp = 0):
    print(sci,eng,hin, sst , comp)
    total = sci + sst + hin + eng + comp
    print(total)

marks()
greet("shijo" , "stephen")