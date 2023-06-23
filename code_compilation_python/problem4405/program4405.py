    from sys import stdin
    from itertools import repeat
def main():
        a, b, h, w, n = map(int, stdin.readline().split())
        m = map(int, stdin.readline().split(), repeat(10, n))
        m.sort(reverse=True)
        m += [1] * 40
    def go(dep, c, hh, ww, a, b):
            if dep >= 20:
                if ww < a and ww < b:
                    return 999
                for i in xrange(20):
                    if hh >= a and ww >= b:
                        return c + i
                    if ww >= a and hh >= b:
                        return c + i
                    hh *= m[i+20]
                return 999
            if hh >= a and ww >= b:
                return c
            if ww >= a and hh >= b:
                return c
            k1 = k2 = 999
            if b > hh or hh < a:
                k1 = go(dep + 1, c + 1, hh * m[dep], ww, a, b)
            if b > ww or ww < a:
                k2 = go(dep + 1, c + 1, hh, ww * m[dep], a, b)
            if k1 < k2:
                return k1
            else:
                return k2
        ans = go(0, 0, h, w, a, b)
        if ans == 999:
            ans = -1
        print ans
    main()