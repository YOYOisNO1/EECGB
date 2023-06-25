def program4817():
    r2=[ 2**i for i in range(31) ]
    r3=[ 3**i for i in range(21) ]
    s=set()
    l, r=map(int, input().split())
    for i in range(31):
        for j in range(21):
            k=r2[i]*r3[j]
            if k<=2*10**9:
                if l<=k<=r:
                    s.add(k)
            else:
                break
    print(len(s))