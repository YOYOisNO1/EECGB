def program2278():
    n = input()
    q = [0]*len(n)
    b = n
    p=""
    y=0
    l=0
    for i in range(len(n)-1,-1,-1):
        p+=n[i]
    y=len(n)-1
    for i in range(len(n)//2):
        if b[i]!=b[y]:
            l+=1
        y-=1
    if p==b and len(n)%2!=0:
        print("YES")
    elif l==1:
       print("YES")
    elif l>1
        print("NO")
    