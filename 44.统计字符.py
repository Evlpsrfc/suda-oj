def func(s):
#your code begin
    vis = dict()
    lst = []
    for ch in s:
        if not vis.get(ch):
            vis[ch] = True
            lst.append(s.count(ch))
    return lst
#your code end
