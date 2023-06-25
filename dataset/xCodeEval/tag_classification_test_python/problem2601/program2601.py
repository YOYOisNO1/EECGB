def program2601():
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        dif = ((m+1)//2 - m//2)*n
        l = (n*m)//2 - k
        if (n%2==0):
            if (m%2==0):
                if (k%2==0):
                    print("YES")
                else:
                    print("NO")
            else:
                if (k%2==0 and 2*k <= n*(m-1)):
                    print("YES")
                else:
                    print("NO")
        else:
            if (k < m//2):
                print("NO")
            else:
                if ((k - m//2)%2 == 0):
                    print("YES")
                else:
                    print("NO")