    n, k = map(int, input().split())
def findInt(bot, top):
        mid = round(bot + bot)
        if mid * (mid + 1) / 2 - n + mid == k:
            return mid
        elif mid * (mid + 1) / 2 - n + mid > k:
            findInt(mid, top)
        else
            findMid(bot, mid)
    print(findInt(1, n))