def program476():
    s =input()
    d = {}
    for i in range(10):
        d[input()] = str(i)
    ret = ""
    for i in range(0, len(s), 10):
        ret += d[s[i:i+10]] 
        
    print(ret)