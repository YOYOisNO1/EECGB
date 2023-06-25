def program2346():
    N = input()
    for i in range(4):
        a,b,c,d = map(int, input().split())
        a=min(a,b)
        if a+min(c,d) <= N:
            print(i+1,a,N-a)
            exit()
    print(-1)