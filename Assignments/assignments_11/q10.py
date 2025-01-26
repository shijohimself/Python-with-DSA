my_list = [4,8,6,19,3,12,1,7,6,2]

def is_prime(lst):
    n = len(lst)
    for num in range(0,n):
        prime = True
        for i in range(2,num):
            if num % i == 0:
                prime = False
                break
        if prime:
            return num
x = is_prime(my_list)

def largest_prime(x):
    n = 0
    if x > n:
        print(x)

largest_prime(x)



