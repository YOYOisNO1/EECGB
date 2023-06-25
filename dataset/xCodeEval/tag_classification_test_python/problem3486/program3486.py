def program3486():
    n,k = map(int, input().split())
    a=map(int, input().split())
    # an=0
    # ann=0
    # i=0
    # for i in range(n):
    #     if an>=k:
    #         break
    #     if ann+a[i]>=8:
    #         ann=ann+a[i]-8
    #         an+=8
    #     else :
    #         an+=ann+a[i]
    #         ann=0
    # if an<k:
    #     print(-1)
    # else:
    #     print(i)
    res=0
    tar=0
    for i in range(n):
        # print(i)
        res += a[i]
        # if res > 8:
        #     tar += 8
        #     res -= 8
        # else:
        #     tar += res
        #     res = 0
        tar += min(res, 8)
        res -= min(res, 8)
        if tar >= k:
            print(i+1)
            exit()
    print(-1)