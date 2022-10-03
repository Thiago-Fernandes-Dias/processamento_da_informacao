def Algorithm(v, m):
    a = [0 for _ in range(0, 5)]
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if a[v[i]] < m[i][j]:
                a[v[i]] += m[i][j]
            else:
                a[v[i]] -= m[i][j]
    return a

result = Algorithm([0, 4, 1, 2, 3], [[1, 7], [9, 9], [3, 6], [6, 6], [5, 6]])
print(*result)