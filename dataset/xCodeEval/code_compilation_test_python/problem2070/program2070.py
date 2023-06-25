def program2070():
    l = list(map(int,input().split())
    k1 = min(l[1]+l[1]+1,l[-2]+l[-2]+1)
    k2 = max(l[1]+l[1]+1,l[-2]+l[-2]+1)
    s1 = 0
    for i in range(k1,k1+2*l[0],2):
        s1 = s1 + i
    for j in range(k2,k2+2*l[5],2):
        s1 = s1 + j
    print(s1)