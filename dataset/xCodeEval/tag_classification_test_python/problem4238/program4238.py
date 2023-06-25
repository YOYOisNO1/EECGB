def program4238():
    k=0
    for i in range(8):
        s=input()
        a=[s[x] for x in range(0,8,2)]
        b=[s[x] for x in range(1,8,2)]
        if a.count(a[0])==4 and b.count(b[0])==4 and a[0]!=b[0]:k+=1
    print(["NO","YES"][k==8])