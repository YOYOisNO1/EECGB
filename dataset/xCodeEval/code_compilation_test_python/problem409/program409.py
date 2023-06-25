def program409():
    n,d = map(int,input().split())
    t = map(int,input().split())
    
    total_t = sum(t)
    current_joke = 10*(n-1)
    current = total_t + current_joke
    left = (d - current)/5
    
    if left > =0:
        print left + (n-1)*2
    else:
        print -1