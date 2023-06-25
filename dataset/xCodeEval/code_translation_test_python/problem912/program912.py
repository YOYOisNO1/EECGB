def program912():
    pstr, d = input().split()
    p, d = int(pstr), int(d)
    n = len(pstr)
    
    ans = pstr
    max9 = n - len(pstr.rstrip('9'))
    for i in range(1, n):
        pcur = p - int(pstr[-i:]) - 1
        if p - pcur > d:
            break
    
        pcur_str = str(pcur)
        nines = len(pcur_str) - len(pcur_str.rstrip('9'))
        if nines > max9:
            max9 = nines
            ans = pcur
    
    print(ans)