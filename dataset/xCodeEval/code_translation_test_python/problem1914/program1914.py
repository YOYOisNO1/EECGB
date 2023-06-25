def program1914():
    from sys import exit
    
    n = int(input())
    P = []
    
    if n >= 38:
        print("0")
        exit()
    
    for i in range(n):
        tmp = input().split()
        tmp = [int(k) for k in tmp]
        P.append(tuple(tmp))
    
    isGood = [True for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(j):
                dp = 0
                for d in range(5):
                    dp += (P[j][d] - P[i][d])*(P[k][d] - P[i][d])
                if dp > 0:
                    isGood[i] = False
    
    print(isGood.count(True))
    for i in range(n):
        if isGood[i]:
            print(i + 1)
                
        