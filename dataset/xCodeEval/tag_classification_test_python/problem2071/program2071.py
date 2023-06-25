    inputlist=list(map(int, input().split()))
    n=inputlist[0]
    k=inputlist[1]
    d=inputlist[2]
def dp(sum1,limiter):
        array=[1]*2
        if limiter==0:
            return 0
        elif limiter==1:
            return 1
        elif limiter==2:
            for j in range(sum1-1):
                array.append(array[len(array)-1]+array[len(array)-2])
            return array[-1]
        else:
            if sum1>limiter:
                for j in range(1, limiter):
                    array.append(2**(j))
                leftpointer=1
                rightpointer=limiter
                s=sum(array[1:])
                array.append(s)
                for j in range(sum1-limiter-1):
                    s-=array[leftpointer]
                    rightpointer+=1
                    s+=array[rightpointer]
                    array.append(s)
                    leftpointer+=1
                return array[-1]
            elif sum1<=limiter:
                return 2**(sum1-1)
    print((dp(n,k)-dp(n,d-1))%(10**9+7))