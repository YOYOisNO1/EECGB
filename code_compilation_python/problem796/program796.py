def program796():
    import collections
    s=input()
    d=input()
    l1=[]
    l2=[]
    a=len(s)
    b=len(s)
    i=0
     while(a):
        l1.append(s[a-1])
        a=a-1
    while(b):
        l2.append(d[i])
        i=i+1
        b=b-1
    if collections.Counter(l1) == collections.Counter(l2):
        print ("YES")
    else :
        print ("NO")