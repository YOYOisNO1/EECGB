def program2241():
    n = input()
    a = map(int, input().split())
    print min(abs(360-2*sum(a[j:i]))for i in range(n)for j in range(i))