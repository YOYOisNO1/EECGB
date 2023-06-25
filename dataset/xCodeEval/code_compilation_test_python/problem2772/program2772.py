def program2772():
    count=sum1=sum2=0
    count1=0
    count2=0
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
    	if a[i]>b[i]:
    		count+=1
    	elif a[i]<b[i]:
    		count1+=1
    	else:
    		count2+=1
    
    if count2==n or count1==n and count==0:
    	print("-1")
    elif count1==0 or count==0:
    	print("1")
    else:
    	if count==1:
    		sum1=count1+count
    		print(sum1)
    	elif count1!=0:
    		final=count1/count+1
    		print(int(final))
    	else
    		print("-1")