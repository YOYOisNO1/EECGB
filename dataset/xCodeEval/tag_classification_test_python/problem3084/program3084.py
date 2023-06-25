def program3084():
    n=int(input())
    s=input()
    k=''
    i=0
    
    while(i<n):
    	if (i!=n-1 and s[i]!=s[i+1]):
    		k+='D'
    		i+=2
    	else:
    		k+=s[i]
    		i+=1
    print(len(k))