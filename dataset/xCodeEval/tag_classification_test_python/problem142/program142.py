def program142():
    n = float(input())
    t = map(int, input().split())
    t = sorted(t)
    st = float(sum(t))
    s = st/n
    if s >= 4.5:
        print('0')
        exit(0)
    for x in range(0, len(t), +1):
        st -= t[x]
        st += 5
        s = st/n
        if s >= 4.5:
            print(x+1)
            exit(0)