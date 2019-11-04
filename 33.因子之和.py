def func(n):
#your code begin
    return sum(filter(lambda x : n % x == 0, range(1, n)))
#your code end
