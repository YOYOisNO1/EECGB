def program2401():
    n,k = input().split()
    k = int(k)
    n = list(n)
    for i in range(len(n)-1):
        jj = maxn = 0
        for j in range(i+1,min(len(n),i+k+1)):
            if int(n[i]) < int(n[j]) and int(n[j]) > maxn:
                maxn = int(n[j])
                jj = jjm,
        if jj > 0:
            n[i],n[jj] = n[jj],n[i]
            k -= jj-i
    print "".join(n)