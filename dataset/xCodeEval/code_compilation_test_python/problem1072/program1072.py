def program1072():
    import re
    t=int(input())
    for _ in range(t):
        n=int(input())
        if(n%2==0):
            print(n//2,n//2)
        elif(n%3==0):
            print(n//3,2*(n//3))
        else
            a=1
            for i in range(4,int(math.sqrt(n))+1):
                if(n%i==0):
                    a=i
                    a=n//a
                    break
            print(a,n-a)
            