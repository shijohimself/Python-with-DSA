def add(*args):
    print(args)

add(1,22,3,4,5)

def add_kwargs(**kwargs):
    print(kwargs)

add_kwargs(name="Shijo",age=24,gender="male")