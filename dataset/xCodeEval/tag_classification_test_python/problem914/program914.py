def program914():
    n = int(input())
    a = map(int, input().split())
    adict = dict()
    for i in xrange(n):
        if a[i] in adict:
            adict[a[i]].append(i)
        else:
            adict[a[i]]=[i]
    flag = [True for i in xrange(n)] #True means have not considered
    target = 2*sum(a)/n
    for i in xrange(n):
        if flag[i]:
            j = adict[target - a[i]].pop()
            flag[j] = False
            flag[i] = False
            print(i+1,) j+1