def program243():
    n = int(input())
    n -= 1
    st = 1
    
    while n-st >= 0:
        n -= st
        st += 1
    
    print(n+1)