def program3588():
    n,t=map(int, input().split())
    S=list(input())
    a=''
    for j in xrange(t):
        b=(i for i in xrange(n-1))
        for i in b:
            if (S[i]=='B') and (S[i+1]=='G'):
                S[i],S[i+1]=S[i+1],S[i]
                try:
                    b.next()
                except StopIteration:
                    break
    for i in xrange(n):
        a=a+str(S[i])
    print(a)