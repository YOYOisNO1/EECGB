def program2305():
    A=[int(i) for i in input().split()]
    Min=min(A)
    A.remove(Min)
    print (((Min-1)+A[0])*((Min-1)+A[1])-(Min-1)*Min)
    #input()