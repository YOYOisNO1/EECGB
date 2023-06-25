def program3573():
    n,t = map(int, input().split())
    s = input()
    for j in range (t):
        S = list(s)
        for i in range (n - 1):
            if(s[i] == 'B'  and  s[i + 1] == 'G'):
                S[i] = 'G'
                S[i + 1] = 'B'
        s = ''.join(S)
    print((s))