def program4286():
    n,l,r,hard = list(map(int,input().split()))
    val = list(map(int,input().split()))
    arr = []
    for i in range(0,2**n):
        x = bin(i)
        x = x.split('b')[1]
        x = '0'*(n-len(x))+x
        arr.append(x)
    ans = 0
    for i in arr:
        if i.count('1')>=2:
            cur = i
            temp = []
            for j in range(n):
                if cur[j]=='1':
                    temp.append(val[j])
            # print(temp)
            p,q = max(temp),min(temp)
            t = sum(temp)
            if (p-q)>=hard and (t>=l and t<=r):
                ans+=1
                # print(i)
    print(ans)