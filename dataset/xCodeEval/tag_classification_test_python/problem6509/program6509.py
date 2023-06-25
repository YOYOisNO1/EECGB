    import math
def make_prime(n):
        flag = [True for _ in range(n+1)]
        p = []
        for i in range(2,n+1):
            if flag[i]:
                p.append(i)
                flag[i]=False
                j = i*2
                while j<=n:
                    flag[j] = False
                    j += i
        return p
def make_count(n,m):
        p = int(math.log(n)/math.log(2))
        flag = [True for _ in range(m*p+1)]
        ans = [0 for _ in range(p+1)]
        s = 0
        for i in range(1,p+1):
            for j in range(1,m+1):
                if flag[i*j]:
                    s+=1
                    flag[i*j]=False
            ans[i]=s
        return ans
def gcd(a,b):
        while a%b!=0:
            r = a%b
            a = b
            b = r
        return b
    
    s = list(map(int,input().split(' ')))
    n,m = s
    prime = make_prime(n)
    #print(len(prime))
    count = make_count(n,m)
    #print(count)
    ans = 1
    flag = [True for _ in range(n+1)]
    for i in range(2,n+1):
        #if i%1000==0:
            #print('current: ', i)
        if flag[i]:
            temp = i
            t = 1
            while temp<=n:
                flag[temp] = False
                temp *= i
                t += 1
            t -=1
            ans += count[t]
        '''
        p_i = []
        temp = i
        flag = True
        for j in prime:
            if temp%j==0:
                t = 0
                while temp%j==0:
                    t+=1
                    temp = temp//j
                if len(p_i)==0:
                    g = t
                    if g==1:
                        break
                    p_i.append([j,t])
                else:
                    g = gcd(g,t)
                    if g==1:
                        break
                    else:
                        p_i.append([j,t])
                if temp==1:
                    break
        if g!=1:
            t = 1
            for j in p_i:
                t *= j[0]**(j[1]//g)
            ans += m-t+1
        else:
            ans += m
        '''
    
    print(ans)