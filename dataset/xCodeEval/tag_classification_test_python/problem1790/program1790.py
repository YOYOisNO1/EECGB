def program1790():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if k >= 2:
        print("Yes")
    else:
        a = [b[-1] if i == 0 else i for i in a]
        print("Yes" if any(a[i] <= a[i-1] for i in range(1, n)) else "No")