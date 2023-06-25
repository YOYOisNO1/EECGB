def program530():
    n = int(input())
    a = list(map(int, input().split()))
    cache = {}
    ans = []
    for i in range(n-1, -1, -1):
    	if not cache.get(a[i]):
    		ans.append(a[i])
    		cache[a[i]] = 1
    ans.reverse()
    print(len(ans))
    print(*ans)