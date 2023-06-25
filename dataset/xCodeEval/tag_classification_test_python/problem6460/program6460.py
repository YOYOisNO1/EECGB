def program6460():
    from sys import stdin
    
    kClr = {"R": 0, "G": 1, "B": 2, "Y": 3, "W": 4}
    kNum = {chr(x): x - ord("1") + 5 for x in range(ord("1"), ord("6"))}
    
    ibuf = stdin.readlines()
    
    s = list(set(ibuf[1].split()))
    t = []
    
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            t.append([])
            if s[i][0] != s[j][0]:
                t[-1].append(1 << kClr[s[i][0]])
                t[-1].append(1 << kClr[s[j][0]])
            if s[i][1] != s[j][1]:
                t[-1].append(1 << kNum[s[i][1]])
                t[-1].append(1 << kNum[s[j][1]])
    
    res = 10
    for i in range(1 << 10):
        for li in t:
            for lj in li:
                if (lj & i) != 0:
                    break
            else:
                break
        else:
            res = min(res, bin(i).count("1"))
    
    print(res)