def program1146():
    from math import ceil
    
    X = list(map(int, input().split()))
    First, Second = list(range(1, ceil((X[0] ** 2) / 2) + 1))[::-1], list(range(ceil((X[0] ** 2) / 2) + 1, X[0] ** 2 + 1))[::-1]
    Total, CheckTotal , Check = [], True , True
    for i in range(X[0]):
        Temp = []
        Check = (True if CheckTotal else False)
        for j in range(X[0]):
            if Check:
                Temp.append(First.pop())
            else:
                Temp.append(Second.pop())
            Check = not Check
        CheckTotal = not CheckTotal
        Total.append(Temp)
    Ans = []
    for i in range(X[1]):
        Case = list(map(int, input().split()))
        Ans.append(str(Total[Case[0]-1][Case[1]-1]))
    print("\n".join(Ans))