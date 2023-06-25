    I=lambda : list(map(int,input().split(' ')))
def path(total,num):
        if total in mem:
            return mem[total]
        if total==0:
            return 1
        else:
            mem[total]=0
            for i in range(1,num+1):
                if total-i>=0:
                    mem[total]+=path(total-i,num)
                else:
                    break
            return mem[total]
        
def ans(n,k,d):
        global mem
        mem={}
        a=path(n,k)
        if d>1:
            mem={}
            b=path(n,d-1)
        else:
            b=0
        return a-b
    n,k,d=I()
    print(ans(n,k,d)%int(10**9+7))