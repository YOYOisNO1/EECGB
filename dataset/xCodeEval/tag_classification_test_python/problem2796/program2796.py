    import sys
def getAndParseInt(num=1):
        string = (sys.stdin.readline()).strip()
        if num==1:
            return int(string)
        else:
            return [int(part) for part in string.split()]
    
def getAndParseString(num=1,delim=""):
        string = (sys.stdin.readline()).strip()
        if num==1:
            return string
        else:
            if delim!="":
                return [part for part in string.split(delim)]
            else:
                return [part for part in string.split()]
    
    w,h = getAndParseInt(2)
    u1,d1 = getAndParseInt(2)
    u2,d2 = getAndParseInt(2)
    
    for cur_h in reversed(range(h+1)):
        w+=cur_h
        if cur_h == d1:
            w+=-u1
        elif cur_h == d2:
            w+=-u2
        w=max(0,w)
    print(w)
    