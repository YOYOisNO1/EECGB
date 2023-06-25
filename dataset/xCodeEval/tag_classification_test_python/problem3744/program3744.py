def program3744():
    n=int(input())
    s=list(input())
    sum=0
    sum2=0
    for i in range(n):
        cnt=0
        sum+=int(s[i])
        #print('sum=',sum)
        sum2=0
        for j in range(i+1,n):
            sum2+=int(s[j])
            #print('sum2=', sum2,s[j])
            if sum2==sum:
                cnt+=1
                sum2=0
    
        if cnt>0 and sum2==0:
            print("YES")
            exit()
    
    print('NO')