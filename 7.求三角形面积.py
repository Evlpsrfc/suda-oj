import math
def func(x1, y1, x2, y2, x3, y3):
#your code begin
    a = math.hypot(x1 - x2, y1 - y2)
    b = math.hypot(x2 - x3, y2 - y3)
    c = math.hypot(x3 - x1, y3 - y1)
    p = (a + b + c) / 2
    return math.floor(math.sqrt(p * (p - a) * (p - b) * (p - c)))
#your code end
