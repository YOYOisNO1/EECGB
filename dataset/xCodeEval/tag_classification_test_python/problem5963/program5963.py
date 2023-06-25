def program5963():
    C, Hr, Hb, Wr, Wb = map(int, input().split())
    ans = 0
    for i in xrange(1000000):
        if C/Wr < i: break
        ans = max(ans, (C/Wr-i)*Hr+(C%Wr+i*Wr)/Wb*Hb)
    for i in xrange(1000000):
        if C/Wb < i: break
        ans = max(ans, (C/Wb-i)*Hb+(C%Wb+i*Wb)/Wr*Hr)
    print(ans)