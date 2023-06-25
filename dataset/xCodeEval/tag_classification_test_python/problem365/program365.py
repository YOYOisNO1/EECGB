def program365():
    n=input()
    z=0
    if(n<=2):
        z=z
    else:
         z=n/2-1 if(n%2==0) else n/2
            
    print(z)