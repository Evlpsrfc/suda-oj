def func(lst):
#your code begin
    return sorted([[s[0], sum(s[1:])] for s in lst], key=lambda x : x[1], reverse=True)
#your code end
