    n,k = map(int, input().split())
    b = list(map(int,input().split()))
    
    s = input()
    
    # print(n,k)
    # print(b)
    # print(s)
    
    INF = 1000*1000*1000+123
    R = [];
    W = [];
    O = [];
    
    for i in range(n):
        if s[i] == 'R':
            R.append(b[i])
        elif s[i] == 'W':
            W.append(b[i])
        else:
            O.append(b[i])
    
    
    R.sort()
    R.reverse()
    
    W.sort()
    W.reverse()
    
    O.sort()
    O.reverse()
    
    # print('--------')
    
    # print("-",)
    
    if k == 1:
        print(-1)
        exit(0)
    
    
def solve(A,B):
        # print("\nsolve");
        # print(A);
        # print(B);
        nA = len(A);
        nB = len(B);
    
        pA = [0 for i in range(nA)]
        pB = [0 for i in range(nB)]
    
        pA[0] = A[0]
        pB[0] = B[0]
    
        for i in range(1,nA):
            pA[i] = pA[i-1] + A[i];
        for i in range(1,nB):
            pB[i] = pB[i-1] + B[i];
    
        # print("pA",pA)
        # print("pB",pB)
    
        res = -1
    
        for i in range(1,min(nA+1,k)):
    
            costA = pA[i-1]
            bNeed = k-i
            if bNeed <= 0 or bNeed > nB: continue
            costB = pB[bNeed-1]
            res = max(res,costA+costB)
        return res
    
    
    res = -1
    if len(R) > 0 and len(O)> 0:
        res = max(res,solve(R,O))
    
    if len(W) > 0 and len(O)> 0:
        res = max(res,solve(W,O))
    
    print(res)
    
    #
    # a = [
    #    6,5,37,10,22,9,2,16,3,3,11,9,5,14,11,3,1,4,6,2,7,
    #     3,7,5,4,8,2,7,13,16,15,9,4,4,2,3,9,5,11,3,7,5,9,
    #     3,8,9,4,10,3,2,7,6,9,3,5,4,6,4,14,3,12,6,8,12,7
    # ]
    #
    # print(a)
    #
    # cnt = [0] * 1000
    #
    # for e in a:
    #     cnt[e] += 1
    #
    # a = set(a)
    # a = sorted(a)
    #
    #
    # for e in a:
    #     print("%d %d"%(e,cnt[e]));