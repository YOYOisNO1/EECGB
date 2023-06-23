def do(i):
        if i == "(":
            return 1
        else:
            return -1
def find(i,idx):
        if i<n-idx:
            return idx+i+1
        else:
            return i-(n-idx)+1
    n = input()
    arr = map(do,input())
    s = [0]*n
    s[n-1] = arr[n-1]
    maxi = 0
    maxv = 0
    for i in range(n-1)[::-1]:
        s[i] = s[i+1] + arr[i]
        if s[i] > maxv:
            maxv = s[i]
            maxi = i
    newv = arr[maxi:]+arr[:maxi]
    if sum(newv) != 0:
        print 0
        print 1,1
    else:
        cnt = 0
        cnt1 = -1
        cnt2 = -1
        maxv1,maxv2 = 0,0
        l1,l2,r1,r2 = 0,0,0,0
        last1,last2 = 0,0
        st = 0
        for i in range(n):
            st += newv[i]
            if st == 0:
                cnt += 1
                cnt1 = -1
                last1 = i+1
    
            elif st == 1:
                cnt1 += 1
                if cnt1 > maxv1:
                    maxv1 = cnt1
                    l1 = last1
                    r1 = i+1
    
                last2 = i+1
                cnt2 = -1
            elif st == 2:
                cnt2 += 1
                if cnt2 > maxv2:
                    maxv2 = cnt2
                    l2 = last2
                    r2 = i+1
        if maxv1>maxv2+cnt:
            print maxv1+1
            print find(l1,maxi),find(r1,maxi)
        else:
            print maxv2+cnt+1
            print find(l2,maxi),find(r2,maxi)