def program150():
    n=input()
    a=map(int,input().split())
    k=0
    while(1):
        n-=a[k%7]
        if n<=0:
            print(k%7+1;break)
        k+=1