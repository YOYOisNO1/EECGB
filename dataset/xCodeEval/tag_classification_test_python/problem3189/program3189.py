def program3189():
    s=input()
    lst=[]
    prev=s[0]
    count=1
    for c in range(1,len(s)):
        if prev==s[c]:
            count+=1
        else:
            lst.append(count)
            count=1
        prev=s[c]
    lst.append(count)
    #print(lst)
    count=0
    for c in lst:
        if c%5!=0:
            count+=(c//5)+1
        else:
            count+=(c//5)
    print(count)