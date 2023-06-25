    n, k = map(int, input().split())
    
def cal(mid):
        return k * mid - ((1 + mid) * mid / 2) + k - mid
    
    if n == 1:
        print(0)
    elif n > (k - 1) * k / 2 + 1:
        print(-1)
    else:
        l, r = 0, k - 2
        while r > l:
            mid = l + r >> 1
            cnt = cal(mid)
            if cnt >= n: r = mid
            else: l = mid + 1
        print(r) + 1