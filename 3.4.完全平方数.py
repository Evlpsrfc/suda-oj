import math
def func(n):
#your code begin
    if n < 0:
        return False
    temp = int(math.sqrt(n))
    return temp * temp == n
#your code end
