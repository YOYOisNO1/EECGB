def program1404():
    k,n,w = map(int,input().split())
    s = (w/2)*(2*k+(w-1)*k)
    s = int(s)
    if s<=n:
        print("0")
    else:    
        print((s - n))