import math
def func(n=1000):
#your code begin
    is_prime = lambda x : x % 2 and all(x % i for i in range(3, math.ceil(math.sqrt(x)), 2))
    cur = 3
    lst = []
    while cur < n:
        if is_prime(cur):
            lst.append(cur)
        cur = ((cur + 1) << 1) - 1
    return lst
#your code end
    
