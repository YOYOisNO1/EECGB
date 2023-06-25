    i = 0
     
def Butt(n, m,i):
      	if  n>m:
       		return n-m
       	if 2*n > m and m-n>1:
       		n-=1
       		i+=1
       		return Butt(n, m, i)
       	if 2*n == m:
       		return i+1
       	if m-n>n:
       		n*=2
       		i+=1
       		return Butt(n, m, i)
    	
    n,m =[int(x) for x in input().split()]
    javab=Butt(n, m, i)
    print(javab)