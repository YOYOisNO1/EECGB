def program4689():
    n,k=[int(i) for i in input().split()]
    s=input().strip()
    s=list(s)
    l=[]
    l1=[]
    for i in range(26):
        l1.append(0)
        l.append(0)
    for i in s:
        l[ord(i)-65]+=1
    f=0
    l1[ord(s[0])-65]=1
    count=1
    for i in s:
        if (count==k and l1[ord(i)-65]==0):
            print(('YES'))
            f=1
            break
        l[ord(i)-65]-=1
        if (l[ord(i)-65]>0):
            if (l1[ord(i)-65]!=1):
                l1[ord(i)-65]=1
                count+=1
        else:
            if (l1[ord(i)-65]!=0):
                l1[ord(i)-65]=0
                count-=1
        if (count>k):
            print(('YES'))
            f=1
            break
    if (f==0):
        print(('NO'))