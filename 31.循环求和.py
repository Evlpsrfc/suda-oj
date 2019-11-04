def func(a, n):
#your code begin
    res, b = 0, a
    for i in range(n):
        res += b
        b = b * 10 + a
    return res
##    return (int(str(a) * (n + 1)) - a * (n + 1)) // 9
#your code end
