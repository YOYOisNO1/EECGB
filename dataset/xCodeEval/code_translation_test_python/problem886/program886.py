def program886():
    n , k = input().split()
    for i in range(int(k)):
        n = int(n)
        n = n-1 if n % 10 else n//10
    print(n)