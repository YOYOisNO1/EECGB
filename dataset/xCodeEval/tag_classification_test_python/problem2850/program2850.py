def program2850():
    x = input()
    y = input()
    ans = []
    for i in range(len(x)):
        if y[i] <= x[i]:
            ans.append(y[i])
        else:
            print(-1)
            quit()
    print(*ans,sep='')