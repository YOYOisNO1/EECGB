def program1865():
    s=input()
    vow=['a','e','i','o','u']
    flag=0
    n=len(s)
    for i in xrange(0,len(s)-1,1):
        if s[i]=='n' or s[i] in vow:
            continue
        if s[i] not in vow and s[i]!='n' and s[i+1] in vow:
            continue
        else:
            flag=1
            break
    if s[n-1] not in vow and s[n-1]!='n':
        flag=1
    if flag==0:
        print("yes")
    else:
        print("no")