    x = int(input())
    h, m = map(int, input().split())
    xh = x // 60
    x = x % 60
    
def lucky(h, m):
        return (h%10 == 7) or (m % 10 == 7)
    hh, mm = h, m
    cnt = 0
    while True:
        if lucky(hh, mm):
            print(cnt)
            break
        hh -= xh
        mm -= x
        if mm < 0:
            hh -= 1
            mm = (mm + 60) % 60
    
        while hh < 0:
            hh += 24
        cnt += 1
    