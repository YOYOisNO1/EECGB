def program3886():
    import math
    for i in range(int(input())):
        n,i=int(input()),2
        while i*i<=n and n%i:
            i=i+1
        if i*i<=n:
            print(int(n/i),int(n-n/i))
        else:
            print(1,n-1)
            
        