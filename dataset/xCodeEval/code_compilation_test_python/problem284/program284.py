def program284():
    n,k=map(int,input().split())
    i=1
    d=0
    scores=input()
    while i<k+1:
        a=format(scores[d:d+2])
        a=int(a)
        print(a)
        if a>9:
            i=i+1
            d=d+3
            b=k
        elif a<10 and a>0:
            i=i+1
            d=d+2
            b=k
        else:
            b=i-1
            break
    while i>k and i<n+1:
        c=format(scores[d])
        c=int(c)
        if c==a and c>0:
            b=b+1
        else:
            b=b
        i=i+1
        d=d+2
    print(b)
    
    import msvcrt
      
    print("Press any key to exit...")
      
    while True:
     if ord(msvcrt.getch()) in [0,256]:
      break