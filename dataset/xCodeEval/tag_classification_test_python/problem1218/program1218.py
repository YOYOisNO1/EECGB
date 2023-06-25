def getSum(n): 
        sum = 0
        while(n > 0): 
            sum += int(n%10) 
            n = int(n/10) 
        return sum
    import sys
    a,b,c=map(int,sys.stdin.readline().split())
    ans=[]
    for i in range(1,82):
        if getSum(b*(i**a)+c)==i and (b*(i**a)+c)<10**9 and (b*(i**a)+c)>0:
            ans.append(b*(i**a)+c)    
    print(len(ans))
    print(*ans)
                
            