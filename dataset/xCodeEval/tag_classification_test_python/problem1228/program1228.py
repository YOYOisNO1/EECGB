def program1228():
    n=int(input())
    print(n,end=" ")
    for i in range(n//2,0,-1):
        if(n%i==0):
            print(i,end=" ")
            n=i