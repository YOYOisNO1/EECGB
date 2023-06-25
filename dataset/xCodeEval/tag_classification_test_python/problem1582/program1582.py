def program1582():
    n = int(input())
    ans = 0
    for i in range(1,n+1) :
        ans = ans + 2**i 
    print(ans)