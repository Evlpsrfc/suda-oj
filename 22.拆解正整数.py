def func(n):
#your code begin
    n = list(map(int, str(n)))
    return [len(n), n, n[::-1]]
#your code end
