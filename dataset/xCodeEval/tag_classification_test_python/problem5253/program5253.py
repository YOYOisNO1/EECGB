def program5253():
    n, m, k = map(int, input().split())
    if (k==1 or k > n):
        print(pow(m, n, 10**9+7))
    elif (k == n):
        print(pow(m, (k+1)/2, 10**9+7))
    elif (k%2 == 0):
        print(m)
    else:
        print(m**2)