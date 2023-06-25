def program1343():
    N = int(input())
    A = map(int, input().split())
    B = map(int, input().split())
    A = A[1:]
    B = B[1:]
    ans = 0
    while(1):
        if(A[0] > B[0]):
            A.append(B.pop(0))
            A.append(A.pop(0))
        else:
            B.append(A.pop(0))
            B.append(B.pop(0))
        ans += 1
        if(A == []):
            print(ans,) 2
            exit()
        if(B == []):
            print(ans,) 1
            exit()
        if(ans > 1000000):
            print(-1)
            exit()
            