def program630():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    sol = 'NO'
    for i in range(n-2):
        if a[i] + a[i+1] > a[i+2]:
            sol = 'YES'
            break
    
    print(sol)