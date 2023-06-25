def program5005():
    s,k=map(int,input().split())
    F = [0,1]
    b = set()
    while True:
        f = sum(F[-k:])
        if f > s:
            break
        F.append(f)
    for i in reversed(F):
        if i <= s:
            b.add(i)
            s -= i
    print(len(b))
    print((') '.join(map(str,b)))
          