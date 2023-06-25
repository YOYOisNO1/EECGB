def program2338():
    if __name__=='__main__':
        n,k = map(int, input().split())
        arr = map(int, input().split())
        if n==k:
            print 0
            return
        ones, twos = [], []
        for i in range(k):
            ones.append(0)
            twos.append(0)
    
        for i in range(n):
            r = i%k
            if arr[i]==1:
                ones[r]+=1
            else:
                twos[r]+=1
    
        ans = 0
        for i in range(k):
            ans += min(ones[i],twos[i])
        print ans