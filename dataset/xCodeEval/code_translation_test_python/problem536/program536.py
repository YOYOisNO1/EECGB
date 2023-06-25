def program536():
    n=input()
    z=0
    for j in (100,20,10,5,1):
        z+=n/j
        n%=j
    print(z)