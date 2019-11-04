def func(n):
# your code begin
    return '\n'.join([('*' * (i << 1 | 1)).center((n << 1) - 1) for i in range(n)])
# your code end
