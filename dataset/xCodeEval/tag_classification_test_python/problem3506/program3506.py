def program3506():
    h1, m1 = map(int, input().split(':'))
    h2, m2 = map(int, input().split(':'))
    t = (h2*60+m2)-(h1*60+m1)
    t //= 2
    q, r = divmod(t, 60)
    if m1+r >= 60:
        q += 1
        r -= 60
    ans = str(h1+q).zfill(2)+':'+str(m1+r).zfill(2)
    print(ans)