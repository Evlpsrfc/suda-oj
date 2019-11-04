dp = {0: 1, 1: 1}
def func(n):
#your code begin
    if dp.get(n):
        return dp[n]
    dp[n] = func(n - 1) + func(n - 2)
    return dp[n]
#your code end
