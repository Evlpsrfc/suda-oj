def func(lst):
#your code begin
    c = lst[0] ^ lst[1]
    return bin(c).count('1')
#your code end
