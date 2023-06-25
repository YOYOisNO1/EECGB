def program608():
    
    from sys import stdin,stdout
    n, m = map(int, stdin.readline().split())
    for i in range(n,-1,-1):
        if ((i *(i+1)*5/2 ) + m ) <= 240:
            print(i)
            break
        