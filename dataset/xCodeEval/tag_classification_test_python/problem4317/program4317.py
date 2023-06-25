def program4317():
    n=input()
    l=len(n)
    mini=-1
    for i in range(1,l-1):
    	for j in range(1,l-1):
       		k=l-i-j
       		if(k>0):
       			# print(i,i+j)
       			t1="".join(n[:i])
       			t2="".join(n[i:i+j])
       			t3="".join(n[i+j:])
       				
       			if((t1[0]=="0" and i>1) or (t2[0]=="0" and j>1) or (t3[0]=="0" and k>1)):
       				continue
       			# print(t1,t2,t3)
       			t1=int(t1)
       			t2=int(t2)
       			t3=int(t3)
       			s=t1+t2+t3
       			if(s>mini and t1<=10**6 and t2<=10**6 and t3<=10**6 ):
       				mini=s
    print(mini)
        