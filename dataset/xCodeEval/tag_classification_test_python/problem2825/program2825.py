def program2825():
    L = lambda: sorted(map(int,input().split()))
    a1,b1 = L(); a2,b2 = L(); a3,b3 = L()
    for a1,b1 in (a1,b1),(b1,a1):
        for a2,b2 in (a2,b2),(b2,a2):
            for a3,b3 in (a3,b3),(b3,a3):
                if max(a2,a3) <= a1 and b2+b3 <= b1:
                    print("YES")
                    exit(0)
    print("NO")