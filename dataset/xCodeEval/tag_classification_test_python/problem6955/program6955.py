    import random
    
    inp = input().split(" ")
    N = int(inp[0])
    P = float(inp[1])
    
    
# def sim1sm(N, P, s):
    #     numTrials = 20000
    #     succ = 0
    #     for _ in range(numTrials):
    #         r = [1]
    #         for _ in range(2):
    #             n = random.randint(s+1,N)
    #             while n in r:
    #                 n = random.randint(1,N)
    #             r.append(n)
    
    #         disc = []
    #         for i in range(3):
    #             if r[i] > s:
    #                 disc.append(r[i])
    #                 break
    #         if len(disc) == 0:
    #             succ += 1
    #             continue
            
    #         sd = random.randint(1, 3)
    #         disc.append(r[sd-1])
            
    #         fc = []
    #         for i in r:
    #             if not i in disc:
    #                 fc.append(i)
            
    #         mcidx = random.randint(1, len(fc))
    #         mc = fc[mcidx - 1]
    #         if mc <= s:
    #             succ += 1
            
    #     return succ/numTrials
    
    l = 0
    r = N
    while(l < r):
        mid = int((l+r)/2)
        expProb = 0.0
        if mid >= 3:
            expProb += ((mid * (mid-1) * (mid-2)) / (N * (N-1) * (N-2)))
        if mid >= 2:
            expProb += (3 * ((N - mid)/N) * (mid/(N-1)) * ((mid-1)/(N-2)))
        if mid >= 1:
            condProb = (3 * (mid/N) * ((N-mid)/(N-1)) * ((N-mid-1)/(N-2)))
            expProb +=  (condProb * (1/3)) + (condProb * (1/3) * (1/2))
    
        if expProb < P:
            l = mid+1
        else:
            r = mid
    
    print(l)
        