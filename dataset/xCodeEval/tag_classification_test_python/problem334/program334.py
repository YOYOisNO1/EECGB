def program334():
    L = [2, 7, 2 , 3, 3, 4, 2, 5, 1, 2]
    n = int(input())
    ans = L[n%10] * L[n/10]
    print(ans)