def program2744():
    /**
     * website: http://codeforces.com/contest/784/problem/B
     * desp: convert to hex, then count the number of zero
     * status: 
     */
    x = input()
    num = hex(int(x))
    s = str(num)[2:]
    # print s
    ans = 0
    cnt = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
    for ch in s:
        if (ch >= '0') and (ch <= '9'):
            now = int(ch)
        if (ch>='a') and (ch <='f'):
            now = 10+ord(ch)-ord('a')
        # print now
        ans = ans+cnt[now]
    print ans