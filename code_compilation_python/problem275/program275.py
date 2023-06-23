def program275():
    n=int(input())
    n=2*n
    s=(input())
    a=[]
    b=[]
    for i in range(n//2):
        a.append(s[i])
    for i in range(n//2,n):
        b.append(s[i])
    a=[int(i) for i in a]
    b=[int(i) for i in b]
    a.sort()
    b.sort()
    a=a[::-1]
    b=b[::-1]
    
    
    if(a[0]<b[0] and a[1]<b[1]):
        print("YES")
        exit()
            
    elif(a[0]>b[0] and a[1]>b[1]):
            print("YES")
            exit()
    
    else:
        print("NO")
    
        