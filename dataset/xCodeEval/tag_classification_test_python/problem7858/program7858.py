def program7858():
    n,s,ans=input(),[],0
    for i in map(int,input().split(' ')):
        while len(s)>1 and min(s[-1],s[-2],i)==s[-1]:
            ans+=min(i,s[-2])
            del(s[-1])
        s.append(i)
    s.sort()
    print(ans+sum(s[0:-2]))