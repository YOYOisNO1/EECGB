def program2555():
    n=input()
    s=input()
    n=int(n)
    t1=len(s)
    k=1
    sum=0
    while t1>0:
        m=0
        for i in range(0,t1):
            if int(s[i:t1])<n:
                m=i
                break
        while m<t1 and s[m]=='0':
            m=m+1
        sum+=k*int(s[i:t1])
        k*=n
        t1=m
    print(sum)