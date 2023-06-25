def inp():
        return int(input())
def linp():
        return map(int, input().split())
    n = inp()
    s = input()
    open = []
    close = []
    for i in xrange(n):
        if s[i]=='(':
            open.append(i)
        if s[i]==')':
            close.append(i)
    li = []
    for i in xrange(len(open)):
        li.append(s[open[i]+1:close[i]])
    lis = ""
    dic={}
    for i in xrange(300):
        dic[i] = 0
    for i in xrange(len(open)):
        for j in xrange(open[i], close[i]+1):
            dic[j] = 1
    for i in xrange(n):
        if dic[i]==0:
            lis+=s[i]
        else:
            if s[i]=='(' or s[i]==')':
                lis+='_'
    maxx = 0
    temp = 0
    for i in xrange(len(lis)):
        if lis[i]=='_':
            maxx = max(maxx, temp)
            temp = 0
        else:
            temp+=1
    maxx=max(maxx, temp)
    print(maxx,)
    cnt=0
    for i in xrange(len(li)):
        tp = 0
        for j in xrange(len(li[i])):
            if li[i][j]=='_':
                if tp>0:
                    cnt+=1
                tp = 0
            else:
                tp+=1
        if tp>0:
            cnt+=1
    print(cnt)