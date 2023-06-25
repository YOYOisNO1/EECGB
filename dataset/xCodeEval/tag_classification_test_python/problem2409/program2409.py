def program2409():
    n=int(input())
    s=input().split('(')
    i,o,ans=[],[],[0]*2
    f=0
    for a,p in enumerate(s):
        if a==0:
            for x in p.split('_'):
                ans[0]=max(ans[0],len(x))
        else:
            t=p.split(')')
            for x in t[0].split('_'):
                if x: ans[1]+=1
            for x in t[1].split('_'):
                ans[0]=max(ans[0],len(x))
    print(ans[0],ans[1])