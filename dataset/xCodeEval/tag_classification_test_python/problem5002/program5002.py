def genkbon (s, k):
        if (k<50):
            i = 0
            res = [0]
            while (res[i]<=s):
                if (i<k):
                    res.append(0)
                elif (i==k):
                    res.append(1)
                elif (i==k+1):
                    res.append(1)
                else:
                    res.append(2*res[i]-res[i-k])
                i += 1
            del res[-1]
            return res
        if (k>=50):
            res = [0,1]
            i = 1
            while (res[i]<=s):
                res.append(2*res[i])
                i += 1
            return res
        
def solve(s, k, tmp):
        tmp2 = tmp
        while (tmp2[-1]>s):
            del tmp2[-1]
        if (s==0):
            return [0]
        if (s==1):
            return [0,1]
        if (s==2):
            return [0,2]
        ha = tmp2[-1]
        res = solve(s-ha,k,tmp2)
        return [ha]+res
        
    inp1 = input()
    inp = inp1.split()
    hlp = genkbon(int(inp[0]),int(inp[1]))
    sol = solve(int(inp[0]),int(inp[1]), hlp)
    print(len(sol))
    for i in sol[:-1]:
        print(i,end=' ')
    print(sol[-1])