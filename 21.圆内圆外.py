import math
def func(lst):
#your code begin
    return "in" if math.hypot(lst[0] - lst[3], lst[1] - lst[4]) <= lst[2] else "out"
#your code end
