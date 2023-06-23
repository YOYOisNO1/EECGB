def program2308():
    A=[int(i) for i in input().split()]
    Min=min(A)
    Max=max(A)
    A.remove(Max)
    A.remove(Min)
    Mid=A[0]
    print (Min+Max)*Mid