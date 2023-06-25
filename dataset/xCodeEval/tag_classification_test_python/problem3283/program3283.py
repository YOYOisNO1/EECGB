def program3283():
    r=lambda:map(int,input().split())
    
    n=input()
    
    t=r()
    c=0
    for i in range(91):
        if i in t:
            c=0
        c+=1
        if c > 15:
            break
    print(i)