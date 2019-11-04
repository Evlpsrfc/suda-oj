def func(m1, m2):
#your code begin
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
#your code end
