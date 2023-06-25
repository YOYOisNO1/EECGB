def program2770():
        n=int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        j=0
        count1=0
        count=0
        if A==B:
            print(-1)
        else:
            for i in range(0,n):
                if A[i]==0 and B[i]==1:
                    count1+=1
                elif A[i]==1 and B[i]==1:
                    count1+=1
                elif A[i]==1 and B[i]==0:
                    count+=1
        if count>0:
            print (abs(count1-count))
        elif count<0 
            print(-1)
            
    
                
                