def func(n):
#your code begin
##    return bin(n).count('1')
    res = 0
    while n != 0:
        res += n & 1
        n >>= 1
    return res
#your code end
