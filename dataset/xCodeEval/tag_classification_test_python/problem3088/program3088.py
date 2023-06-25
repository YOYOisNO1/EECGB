def program3088():
    n=list(map(int,input().split()))
    if(n[1]>=(n[0]-1)):
        print(n[0]-1)
    else:
       w=n[1]
       for i in range(2,(n[0]-n[1])+1):
           w=w+i
       print(w)
           
    