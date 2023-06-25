def program6921():
    inp = input()
    intinp = int(inp,2)
    
    ret = 0
    clen = 0
    for i in range(len(inp)):
        if(inp[len(inp)-1-i] == '1'):
            ret += 2**(2*clen + len(inp) - 1 - i)
            ret %= 1000000007
        clen += 1
    print(ret)
    