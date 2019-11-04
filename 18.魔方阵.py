def func(n):
#your code begin
    lst = [[0 for j in range(n)] for i in range(n)]
    row, col = 0, n // 2
    lst[row][col] = 1
    for i in range(2, n * n + 1):
        n_row, n_col = (row + n - 1) % n, (col + 1) % n
        if lst[n_row][n_col] or row == 0 and col == n - 1:
            n_row, n_col = row + 1, col
        row, col = n_row, n_col
        lst[row][col] = i
    return lst
#your code end
