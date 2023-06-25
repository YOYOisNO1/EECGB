def program3025():
    import math
    from collections import Counter
    a = input()
    b = input()
    d = Counter((a.strip()))
    s = d['+'] - d['-']
    d = Counter(b.strip())
    pos = d['?']
    s -= d['+'] - d['-']
    if pos == s:
        return 1
    else:
        if (pos - math.abs(s)) % 2 == 0:
            return (math.factorial(pos)/(math.factorial((pos + s)/2) * math.factorial((pos - s)/2)))/(2 ** pos)
        else:
            return 0