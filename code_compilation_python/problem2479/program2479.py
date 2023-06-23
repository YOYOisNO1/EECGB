def program2479():
    n, k = map(int, input().split())
    r = map(int, input().split())
    for x in [i for i in range(1, 2 * n) if r[i - 1] + 1 < r[i] and r[i] > r[i + 1] + 1][ : k]:
    	r[x] -= 1
    print ' '.join(map(str, r))