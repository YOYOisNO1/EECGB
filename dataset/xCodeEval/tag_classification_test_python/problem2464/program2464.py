def program2464():
    n = int(input())
    s = input()
    inparenCnt = 0
    ret = 0
    inParen = False
    l = 0
    for i in xrange(n):
        if s[i] == '(':
            inParen = True
            ret = max(ret, l)
            l = 0
        elif s[i] == ')':
            inParen = False
            if l != 0:
                inparenCnt += 1
            l = 0
        elif s[i] == '_':
            if inParen:
                if l != 0:
                    inparenCnt += 1
            else:
                ret = max(ret, l)
            l = 0
        else:
            l += 1
    ret = max(ret, l)
    print(ret,) inparenCnt