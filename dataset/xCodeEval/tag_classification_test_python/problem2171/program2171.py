def program2171():
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    count_a = [0 for _ in xrange(6)]
    count_b = [0 for _ in xrange(6)]
    ans = 0
    for x in a:
        count_a[x]+=1
    for x in b:
        count_b[x]+=1
    for x in xrange(5):
        if (count_a[x+1]+count_b[x+1])%2 != 0 :
            print(-1)
            exit()
        elif count_a[x+1]>=(count_a[x+1]+count_b[x+1])/2:
            ans = ans + count_a[x+1]-(count_a[x+1]+count_b[x+1])/2
    print(ans)
    