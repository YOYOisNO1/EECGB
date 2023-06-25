    F = [1];
    while len(F) <= 13:
        F.append(F[-1]*len(F));
    
def get_perm(k,S):
        if k >= F[len(S)]:
            print(-1;)
            exit(0);
        P = [];
        while k:
            i = 0;
            while F[len(S)-1]*(i+1) <= k:
                i += 1;
            k -= F[len(S)-1]*i;
            P.append(S[i]);
            S.pop(i);
        P += S;
        return P;
    
    q = [0];
    lucky = [];
    while len(q):
        u = q.pop(0);
        if u > 10**9: continue;
        if u: lucky.append(u);
        q.append(u*10 + 4);
        q.append(u*10 + 7);
    
    n,k = map(int,input().split());
    k -= 1;
    while len(lucky) and lucky[-1] > n:
        lucky.pop();
    
    L = min(13,n);
    s = n - L + 1;
    e = n;
    ans = 0;
    while len(lucky) and lucky[0] < s:
        ans += 1;
        lucky.pop(0);
    
    
    P = get_perm(k,range(s,e+1));
    for i in xrange(L):
        if (i + s) in lucky and P[i] in lucky:
            ans += 1;
    print(ans;)