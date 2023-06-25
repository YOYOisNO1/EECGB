def program7079():
    #import random
    
    n = int(input())
    w = list(map(int, input().split()))
    #n = random.randint(2,50)
    #w = [random.randint(1,100) for _ in range(2*n)][:-2]
    
    h = dict()
    for val in w:
        h[val] = h.get(val, 0)+1
    
    res = []
    for key in h:
        res += [key]*(h[key]%2)
    
    res.sort()
    s = []
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            b = res[:i] + res[i+1:j] + res[j+1:]
            s.append(abs(sum(b[::2])-sum(b[1::2])))
    print(min(s))