def program1109():
    s=input()
    a=len(s)
    s=s+'0'
    p=0
    c=s[0]
    i=0
    cnt = 0
    while p < a:
        p+=1#pointer of string
        i+=1
        if s[p] != c:
            cnt+=1
            i=0#number of stuff on his hands
            c=s[p]
        if i==5:
            i=0
            cnt+=1
            c=s[p]
        #print(i, s[p])
    if i != 0:
        cnt+=1
    print(cnt)