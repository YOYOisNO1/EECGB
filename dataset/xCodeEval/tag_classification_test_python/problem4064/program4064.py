def program4064():
    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))
    a.sort()
    print('YES' + '\n' + str(a[0]) +' '+ str(a[n - 1]) if a[0] == a[n // 2 - 1] and a[n // 2] == a[n - 1] and a[0] != a[
        n - 1] else 'NO')