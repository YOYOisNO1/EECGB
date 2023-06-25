def program2112():
    n=int(input())
    binary=list(map(int,input().split()))
    single1=binary.count(1)
    if single1==len(binary):
        print(single1-1)
    """else:
        s=0
        sum1=-200
        finalsum=0
        #replace is not done for list containing integers.Only for strings.
        for i in binary:
            if i==1:
                s=0
                
            else:
                s+=1
                sum1=max(s,sum1)
                finalsum=max(finalsum,sum1)
        print(single1+finalsum)"""
    else:
        s=[]
        for i in binary:
            if i==1:
                s.append(-1)
            else:
                s.append(1)
        sum1=0
        sum2=-2000
        for i in s:
            sum1+=i
            if sum1<0:
                sum1=0
            sum2=max(sum2,sum1)
        print(sum2+single1)
                
            
            