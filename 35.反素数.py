import math
def func(n):
#your code begin
    is_prime = lambda x : x % 2 and all(x % i for i in range(3, int(math.sqrt(x)) + 1, 2))
    cur = 13
    lst = []
    while len(lst) < n:
        if is_prime(cur) and str(cur) != str(cur)[::-1] and is_prime(int(str(cur)[::-1])):
            lst.append(cur)
        cur += 1
    return lst
#your code end
