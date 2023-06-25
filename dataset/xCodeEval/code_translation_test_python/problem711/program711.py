def program711():
    import math
    
    k, n, s, p = input().split()
    paperEachNeed = math.ceil(float(n) / float(s))
    totalPapers = paperEachNeed * float(k)
    packsToBuy = math.ceil(totalPapers / float(p))
    print(int(packsToBuy))