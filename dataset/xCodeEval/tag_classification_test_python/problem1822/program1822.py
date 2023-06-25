def program1822():
    import math
    n=int(input())
    kk=[]
    for i in range(30):
        if 5*((2**i)-1)<=n and 5*((2**(i+1))-1)>n:
            kk.append(i)
            break
    if n==1:
           print("Sheldon")
    elif n==2:
           print("Leonard")
    elif n==3:
           print("Penny")
    elif n==4:
           print("Rajesh")
    elif n==5:
           print("Howard")
    else:
       k=int(kk[0])
       p=2**(k)
       q=n-5*(2**(k)-1)
       r=math.ceil(q/p)
       if r==1:
           print("Sheldon")
       elif r==2:
           print("Leonard")
       elif r==3:
           print("Penny")
       elif r==4:
           print("Rajesh")
       elif r==0 or r==5:
           print("Howard")