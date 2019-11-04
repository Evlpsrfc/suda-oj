def func(n):
#your code begin
##    return n + (n % 100 + 10) % 100 - n % 100 + (n % 1000 + 100) % 1000 - n % 1000
    n = list(map(int, str(n)))
    for i in (1, 2):
        n[i] = (n[i] + 1) % 10
    return int(''.join(map(str, n)))
#your code end
