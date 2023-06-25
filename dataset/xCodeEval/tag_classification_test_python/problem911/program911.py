def lcs(a, b):
        lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
        # row 0 and column 0 are initialized to 0 already
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                if x == y:
                    lengths[i+1][j+1] = lengths[i][j] + 1
                else:
                    lengths[i+1][j+1] = \
                        max(lengths[i+1][j], lengths[i][j+1])
        return lengths[len(a)][len(b)]
    
    factors = []
    
    i = 2
    while (8*i) < 1000:
        factors.append(str(8*i))
        i +=1
    
    
def solve(s):
        if "0" in s:
            return "0"
        if "8" in s:
            return "8"
        for f in factors:
            if lcs(s,f) == len(f):
                return f
        return None
    
    s = input()
    
    ans = solve(s)
    
    if ans == None: print("NO")
    else:
        print("YES")
        print(ans)