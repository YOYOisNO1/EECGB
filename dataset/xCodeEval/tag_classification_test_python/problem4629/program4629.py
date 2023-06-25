def program4629():
    n,k=map(int, input().split())
    s=input()
    l=[[-1,-1] for i in xrange(26)]
    for i in xrange(len(s)):
    	if  l[ord(s[i])-65][0]==-1:
    		l[ord(s[i])-65][0]=i
    		l[ord(s[i])-65][1]=i
    	else:
    		l[ord(s[i])-65][1]=i
    p=[]
    q=[]
    for i in l:
    	if i[0]!=-1:
    		p.append(i[0])
    		q.append(i[1])
    p=sorted(p)
    q=sorted(q)
    #print(p)
    #print(q)
    cnt=0
    i=j=c=0
    while i<len(p):
    	if p[i]<q[j]:
    		c+=1
    		i+=1
    	elif p[i]>q[j]:
    		c-=1
    		j+=1
    	else:
    		cnt=max(cnt,c+1)
    		i+=1
    		j+=1
    	cnt=max(cnt,c)
    #	print(cnt,)
    #print(if) cnt>k:print('YES')
    else:print('NO')