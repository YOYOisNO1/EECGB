def program3955():
    w, m = map(int, input().split())
    if w < 4:
        print('YES')
    else:
        v = []
        while m > 0:
            v.append(m % w)
            m //= w
        v.append(0)
        for i in range(len(v)):
            if (i + 1 < len(v)):
                v[i + 1] += v[i] // w
            v[i] %= w
            if v[i] + 1 == w:
                v[i + 1] += 1
            elif v[i] > 1:
                print('NO')
                break
        else:
            print('YES')