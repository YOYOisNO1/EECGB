def program2172():
    c2 = map(int,input().split())
    c1 = map(int,input().split())
    a = map(int,input().split())
    s = 0
    if c2[1]>c1[1]:
        s+=a[1]
    if c2[1]<0:
        s+=a[0]
    if c2[0]>c1[0]:
        s+=a[5]
    if c2[0]<0:
        s+=a[4]
    if c2[2]>c1[2]:
        s+=a[3]
    if c2[2]<0:
        s+=s[2]
    
    print s