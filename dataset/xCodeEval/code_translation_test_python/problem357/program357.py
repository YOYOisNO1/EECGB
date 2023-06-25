def program357():
    n=int(input())
    arr=[]
    cnt=0
    if n%2==1:
        cnt+=1
        f=0
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                f=1
                n-=i
                break
        if f==0:
            n=0
    print(cnt+n//2)