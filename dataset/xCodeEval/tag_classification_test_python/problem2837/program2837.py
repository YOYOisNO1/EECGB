def program2837():
    n = int(input())//2
    l1 = list(input())
    const = l1.count("x")-l1.count("X")
    ans=0
    while l1.count("X")-l1.count("x")!=0:
        if l1.count("X")>l1.count("x"):
            l1[l1.index("X")]="x"
        else:
            l1[l1.index("x")]="X"
        ans+=1
    print(ans)
    print("".join(l1))
        