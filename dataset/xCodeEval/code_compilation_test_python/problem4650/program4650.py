    from fractions import gcd
def main():
        m, a, b = map(int, input().split())
        l = max(a, b) * 2
        s = [0] * (l + 1)
        ans = 1
        t = 1
        st = []
        pu = st.append
        po = st.pop
        s[0] = 1
        for i in xrange(1, l + 1):
            if s[i-a]:
                pu(i)
                while st:
                    x = po()
                    s[x] = 1
                    t += 1
                    if x + a <= i and not s[x+a]:
                        pu(x + a)
                    if x - b >= 0 and not s[x-b]:
                        pu(x - b)
            ans += t
            if i >= m:
                break
        g = gcd(a, b)
        if m > i:
            p, q = divmod(m - i + 1, g)
            ans += (t + t + p - 1) * p / 2 * g + (t + p) * q - t
        print ans
    main()