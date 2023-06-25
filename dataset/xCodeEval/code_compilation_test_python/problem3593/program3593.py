def program3593():
    Z='IMPOSSIBLE'
    I=input
    k=int(I())
    s=list(I())
    p=s[::-1]
    for i in range(len(s)):
    	if s[i]==p[i]:continue
    	if s[i]=='?':s[i]=p[i]
    	elif p[i]=='?':p[i]=s[i]
    	else:print(Z);exit()
    d=set(chr(i)for i in range(97,97+k)if chr(i) not in s)
    for i in range(len(s)//2+len(s)%2,-1,-1):
    	if len(d) and s[i]=='?':s[i]=s[len(s)-i-1]=max(d);d.remove(max(d))
    s=''.join(s).replace('?','a')
    print([Z,s][set(s)==set(chr(i)for i in range(97,97+k))])