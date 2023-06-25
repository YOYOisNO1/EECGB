    import math
    
    
def cal(ss):
        c = 1
        for j in range(10):
            c *= len(ss[j])
        return c
    
    
    n = int(input())
    if n != 0:
        nn = math.floor(math.log2(n))
        init = "codeforces"
        s = list("codeforces")
        c = 0
        lop = 1 + nn//10
        i = 0
        while i < 10:
            s[i] = list(s[i])*lop
            i += 1
    
        i = 0
        while cal(s) < n:
            s[i] = s[i] + list(init[i])
            i = (i+1) % 10
        i = 0
        while i < 10:
            s[i] = "".join(s[i])
            i += 1
    
        print("".join(s))