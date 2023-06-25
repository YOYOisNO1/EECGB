def program6804():
    Z='IMPOSSIBLE'
    R=range
    P=print(I=input)
    k=int(I())
    s=list(I())
    n=len(s)
    for i in R(n):
    	if s[i]==s[n-i-1]:pass
    	elif s[i]=='?':s[i]=s[n-i-1]
    	elif s[n-i-1]=='?':s[n-i-1]=s[i]
    	else:P(Z);exit()
    d=set(chr(i)for i in R(97,97+k)if chr(i) not in s)
    for i in R(n//2,-1,-1):
    	if len(d) and s[i]=='?':s[i]=s[n-i-1]=max(d);d.remove(max(d))
    s=''.join(s).replace('?','a')
    P([Z,s][set(s)==set(chr(i)for i in R(97,97+k))])