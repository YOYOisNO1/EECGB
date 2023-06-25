def program1773():
    s=input()
    t=input()
    le = len(s)-len(t)
    flag=0
    l=0
    if s==t:
        print(0)
    else:
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                s1 = s[:i]+s[j:]
                count=0
                for ch in t:
                    if ch in s1:
                        lst = list(s1)
                        ind = lst.index(ch)
                        s1 = s1[ind+1:]
                        count += 1
                if count==len(t):
                    leng = j-i
                    if leng>l:
                        l=leng
            le -= 1
        print(l)        