def program6827():
    a = [0]*26
    k = int(input())
    s = input()
    sl = [i for i in s]
    for i in s:
        if(i!='?'):
            a[ord(i)-97] = 1
    for i in range(len(s)//2,len(s)):
        if(s[i]=='?'):
            if(s[len(s)-i-1] == '?'):
                f = 0
                for j in range(k-1,-1,-1):
                    if(a[j]!=1):
                        f = 1
                        sl.pop(i)
                        sl.insert(i,chr(j+97))
                        sl.pop(len(s)-i-1)
                        sl.insert(len(s)-i-1,chr(j+97))
                        a[j] = 1
                        break
                if(not f):
                    sl.pop(i)
                    sl.insert(i,'a')
                    sl.pop(len(s)-i-1)
                    sl.insert(len(s)-i-1,'a')
            else:
                sl.pop(i)
                sl.insert(i,s[len(s)-i-1])
        else:
            if(s[len(s)-i-1] == '?'):
                sl.pop(len(s)-i-1)
                sl.insert(len(s)-i-1,s[i])
    #print(a)
    for i in range(k):
        if(a[i]==0):
            print("IMPOSSIBLE")
            exit(0)
    
    for i in range(len(s)):
        if(sl[i]=='?'):
            sl.pop(i)
            sl.insert(i,'a')
    #print(sl)
    if(sl == sl[::-1]):
        ans = ''
        for i in sl:
            ans+=i
        print(ans)
    else:
        print("IMPOSSIBLE")