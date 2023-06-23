def go(n, c1, c2):
        l = len(n)
        pos2 = n.rfind(c2)
        pos1 = n.rfind(c1)
        if c1 == c2:
            pos1 = n[:pos2].rfind(c1)
        if pos1 == -1 or pos2 == -1:
            return 10 ** 10
        #print(pos1, pos2)
        nxt = 0
        if min(pos1, pos2) == 0:
            nxt = 1
            if max(pos1, pos2) == 1:
                nxt = 2
        ans = 0
        while n[nxt] == '0':
            ans += 1
            nxt += 1
        ans += l - pos2 - 1
        if pos1 > pos2:
            pos1 -= 1
        ans += (l - pos1 - 2)
        return ans
    
    n = input()
    ans = min([go(n, '2', '5'), go(n, '0', '0'), go(n, '7',  '5'), go(n, '5', '0')])
    if ans == 10 ** 10:
        print(-1)
    else:
        print(ans)