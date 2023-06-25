def program1798():
    n=int(input())
    a = list(map(int,input().split()))
    
    b = [0 for i in range(int(max(a)+1))]
    
    for ai in a:
        b[ai]+=1
    
    for i in range(len(b)):
        for k in range(int(b[i])):
            print(i, end=" ")