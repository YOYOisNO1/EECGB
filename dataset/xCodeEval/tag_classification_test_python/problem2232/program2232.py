def program2232():
    r=lambda:map(int,input().split())
    n=input()
    a=r()
    p=-1
    R=int(1 in a)
    for i in range(n):
        if a[i]:
            if p >=0:
                R*=i-p
            #print(i,R,i-p)
            p=i
            
    print(R)