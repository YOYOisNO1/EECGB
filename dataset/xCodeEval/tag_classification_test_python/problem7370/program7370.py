def program7370():
    import sys
    n,k=[int(f)for f in input().split()]
    s = input()
    ans = 0
    rng=n-k+1
    if rng>n:
        rng=n
    for i in range(0, rng) :
        ok = 0
        if i>0:
            if s[i-1]=='N':
                ok=1
        if i+k<n:
            if s[i+k]=='N':
                ok=1
        for j in range(i, i + k) :
            if s[j] == 'Y' :
                ok = 1
        if ok == 0 :
            ans = 1
    if ans == 0 :
        print("NO")
        sys.exit(0)
    ans=0
    for i in range(0,n):
        cnt=0
        mul=1
        for j in range(i,n):
            if s[j]=='N':
                cnt+=mul
            if s[j]!='N':
                mul=0
        if cnt>k:
            ans=cnt
    if ans>0:
        print("NO")
    if ans==0:
        print("YES")