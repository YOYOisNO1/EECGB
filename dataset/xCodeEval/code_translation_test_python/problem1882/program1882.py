def program1882():
    n,a=input(),map(int,input().split(' '))
    s=[]
    ans=0
    for i in a:
        while len(s)>1 and s[-1]<=i and s[-2]>=s[-1]:
            ans+=min(i,s[-2])
            del(s[-1])
        s.append(i)
    s.sort()
    print(ans+sum(s[0:-2]))