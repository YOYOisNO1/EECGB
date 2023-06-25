def program497():
    n= input()
    k= input()
    n=int(n)
    k=int(k)
    lis= input().split(" ")
    p=lis
    length=0
    for i in range(0,k-1):
    	b= list([lis[t] for t in range(0,k) if((t-i)%k!=0) ])
            l= [lis[j] for j in b if(b[j]==-1) ]
    	lent =len(b)-len(l)
    	le=abs(len(l)-lent)
    	if(le>lenghth):
    		length=le
    
    print length