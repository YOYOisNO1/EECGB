def program2599():
    t = int(input())
     
    for c in range(0,t):
        n, m, k = map(int, input().split())
        if(n%2 == 1):
            if((((n*m/2)-k)%m)%2 == 0 and m <= 2*k): print('YES')
            else: print('NO')
    
        else:
            if(m%2 == 0):
                if((k%n)%2 == 0): print("YES")
                else: print('NO')
            else:
                if((k%n)%2 == 0 and 2*k <= n*m-n): print("YES")
                else: print('NO')