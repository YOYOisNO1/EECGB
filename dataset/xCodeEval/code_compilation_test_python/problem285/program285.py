def do():
        n = int(input())
        fromN = 0
        for i in range(n):
            l, d = map(str,input().split())
            l = int(l) % 40000
            fromN %= 40000
            if fromN == 0 and d[0] in "NEW": return "NO"
            if fromN == 20000 and d[0] in "SEW": return "NO"
            if d[0] in "EW": continue
            if d[0] == "N":
                if fromN >= 0 and fromN <= 20000: fromN -= l
                else: fromN += l
            else:
                if fromN >=0 and fromN <= 20000: fromN += l
                else: fromN -= l
            #print(fromN)
            fromN %= 40000
        if fromN == 0: return "YES"
        return "NO"
    
    print(do())