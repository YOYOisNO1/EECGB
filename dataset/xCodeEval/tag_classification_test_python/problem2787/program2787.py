def program2787():
    
    n = int(input())
    A = list(map(int, input().split()))
    
    found = False
    
    if sum(A) != 0:
        print("YES")
        print("1")
        print("1 " + str(len(A)))
        found = True
    else:
        for i in range(len(A)):
            if sum(A[:i]) != 0 and sum(A[i:]) != 0:
                print("YES")
                print("2")
                print("1 " + str(i))
                print(str(i + 1) + " " + str(len(A)))
                found = True
                break
    
    if not found:
        print("NO")
    