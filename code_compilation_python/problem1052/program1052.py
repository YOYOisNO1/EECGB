    import re
    n = int(input())
    
def getDiff(a, b):
        delta = a-b
        if a == b:
            ret = 0
        else:
            aux = abs(delta)%(25-delta)
            if aux == 0:
                ret = 1
            else:
                ret = aux
        return ret
    
    
    # 4
    s = input()
    # WERT
    splited = list(re.findall(r'[A-Z]{4}', s)) + list(re.findall(r'[A-Z]{4}', s[1:])) + list(re.findall(r'[A-Z]{4}', s[2:])) + list(re.findall(r'[A-Z]{4}', s[3:]))
    splited = set(splited)
    # print(splited)
    minn = 99999999999999999
    A = ord('A')
    C = ord('C')
    T = ord('T')
    G = ord('G')
    
    for seq in splited:
        sm = getDiff(ord(seq[0]), A) + getDiff(ord(seq[1]), C) + getDiff(ord(seq[2]), T) + getDiff(ord(seq[3]), G)
        minn = min(minn, sm )
    print(minn)