def func(lst):
#your code begin
    return max(filter(lambda x: x != max(lst), lst))
#your code end
