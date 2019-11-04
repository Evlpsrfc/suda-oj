def func(lst):
#your code begin
    lst.sort()
    length = len(lst)
    if length & 1:
        return lst[length >> 1]
    length >>= 1
    return (lst[length - 1] + lst[length]) / 2
#your code end
