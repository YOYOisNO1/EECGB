def program380():
    n = int(input())
    l = [map(int, input().split()) for i in xrange(3)]
    n -= sum([x[0] for x in l])
    ans = []
    for x in l:
        ans.append(min(n, x[1]))
        n -= ans[-1]
    for i in xrange(3):
        ans[i] += l[i][0]
        
    prnit ' '.join(map(str, ans))