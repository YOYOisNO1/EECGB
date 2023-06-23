def program1673():
    X, Students = list(map(int, input().split())), list(map(int, input().split()))
    for i in range(X[0]):
        Count, Temp, Sum = 0, X[1], sum(Students[:i]) + Students[i]
        if Sum <= X[1]:print(0, end=" ")continue
        else:
            STemp = sorted(Students[:i], reverse=True)
            for j in range(i):
                if X[1] >= Sum:break
                Count, Sum = Count + 1, Sum - STemp[j]
        print(Count, end=" ")
    
    # Come together for getting better !!!!