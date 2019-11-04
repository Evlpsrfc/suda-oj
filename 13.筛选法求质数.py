def func(MAXN=500):
#your code begin
    prime = []
    vis = dict()
    for i in range(2, MAXN):
        if not vis.get(i):
            prime.append(i)
        for p in prime:
            if i * p >= MAXN:
                break
            vis[i * p] = True
            if i % p == 0:
                break
    return prime
#your code end
