def program1765():
    N,K,X = map(int,input().split())
    lst = sorted([int(i) for i in input().split()])
    
    total = 0
    
    for i in range(K):
        total += lst[i] + X
    print(total)
    