def program2775():
    t=int(input())
    for _ in range(t):
        n=int(input())
        c=0
        a=7
        temp=n
        while(temp>0 && a>=2):
            c+=temp//a
            temp%=a
            a-=1
        print(c)