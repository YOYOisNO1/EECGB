def program3045():
    a,b,c=map(int,input().split())
    n1=a//3
    n2=b//2
    n3=c//2
    r=min(n1,n2,n3)
    a-=r*3
    b-=r*2
    c-=r*2
    d={}
    l=['f','r','c','f','c','r','f']
    if a>=b and a>=c:
    	if b>c and a>b+1:
    		k=5
    	elif b>=c and a<b+1:
    		k=3
    
    	elif c>b and a>c+1:
    		k=6
    	elif c>b and a<=c+1:
    		k=0
    else:
    	if b>=c:
    		k=4
    	else:
    		k=1
    d['f']=a
    d['r']=b
    d['c']=c
    count=0
    for i in range(k,k+7):
    	e=i%7
    
    	if d[l[e]]>0:
    		d[l[e]]-=1
    		count+=1
    	else:
    		break
    
    
    print(count+r*7)