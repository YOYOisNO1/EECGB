def program2476():
    n=int(input())
    s=input()
    flag=0
    br=[]
    xs=[]
    i=0
    while(True):
    	end=s.find('(',i)
    	if(end==-1):
    		ne=s[i:]
    		xs.extend(ne.split('_'))
    		break
    	#print(type(i),type(end))
    	ne=s[i:end]
    	xs.extend(ne.split('_'))
    	i=end+1
    	end=s.find(')',i)
    	ne=s[i:end]
    	br.extend(ne.split('_'))
    	i=end+1
    xs.sort(key = lambda s: len(s),reverse=True)
    print(len(xs[0]))
    count=0
    for i in br:
    	if(len(i)>0):
    		count+=1
    print(count)