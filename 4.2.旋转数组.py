def func(lst, k):
#your code begin
    _lst = lst.copy()
    length = len(lst)
    for i in range(length):
        _lst[(i + k) % length] = lst[i]
    return _lst
#your code end
