def program1321():
    for t in range(int(input())):
        n=int(input())
        test=0
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                test=1
                break
        if test==1:
            
            a=n//i
            b=n-a
        else:
            a=1
            b=n-1
        print(a,b)
        