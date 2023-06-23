def program1398():
    a = int(input())
    A = list(map(int, input().split()))
    
    b = True
    for i in range(a-1):
        if (abs(A[i+1]-A[i])>1):
            b = False
            break
    if (b):
        print(“YES”)
    else:
        print(“NO”)