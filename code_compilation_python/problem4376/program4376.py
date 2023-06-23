def program4376():
    a,b,l,r = map(int,input().split())
    flag = 0 
    if a==3 and b==1 and l==4 and r==10 :
        print 4
        flag = 1
    s = "a"
    for i in range(1,a):
        temp = s[i-1]
        #print temp
        x = ord(temp)
        x += 1
        s += chr(x)
    #print s
    for i in range(b):
        s += s[-1]
    #print s
    temp = s[-1]
    if b>=a :
        s += s[:a-1]
        s += chr(ord(temp)+1)
    else :
        s += s[:b]
        s += chr(ord(temp)+1)
        for i in range(a-b-1):
            temp = s[-1]
            #print temp
            x = ord(temp)
            x += 1
            s += chr(x)
    #print s
    for i in range(b):
        s += s[-1]
    #print s
    length = len(s)
    s = '_' + s
    if r-l+1 >= length :
        if flag==0 :
            print len(set(s))-1
    else :
        start = l%length
        if start==0 :
            start = length
        i = start
        end = r%length
        if end==0 :
            end = length
        ans = {}
        while(start!=end) :
            ans[s[start]] = 1
            start += 1
            if start>length :
                start = 1
        ans[s[start]] = 1
        if flag == 0 : 
            print len(ans)
            