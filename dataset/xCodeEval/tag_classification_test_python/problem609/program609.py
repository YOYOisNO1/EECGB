def program609():
    n,k = list(map(int,input().split()))
    k = 240-k
    time_i = 0
    count = 0
    for i in range (1,n+1):
        if time_i +(5*i) > k:
            break
        else:
            time_i+=(5*i)
            count+=1
    print(count)