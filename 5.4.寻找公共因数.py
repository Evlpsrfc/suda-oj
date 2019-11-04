import math
def func(a, b):
#your code begin
    g = math.gcd(a, b)
    return list(filter(lambda x: g % x == 0, range(1, g + 1)))
#your code end
