def program2966():
        n = input()
        k = list(set(map(int, input().split())))
        if len(k) == 1:
            print("NO")
            exit()
        for i in xrange(len(k)-1):
            if k[i+1] < k[i]*2:
                print("YES")
                exit()
        print("NO")