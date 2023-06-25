def program4583():
    from collections import Counter
    n = int(input())
    A = list(map(int, input().split()))
    cnt = Counter(A)
    maxv = max(cnt.values())
    x = [c for c in cnt if cnt[c] == maxv]
    if len(x) > 1:
        print(n)
    else:
        x = x[0]
        ans = 0
        for c in cnt:
            if c == x: continue
            dic = {0: -1}
            cur = 0
            tmp = 0
            for i, a in enumerate(A):
                cur += 1 if a == c else -1 if a == x else 0
                if cur in dic:
                    tmp = max(tmp, i - dic[cur])
                dic.setdefault(cur, i)
            ans = max(ans, tmp)
        print(ans)