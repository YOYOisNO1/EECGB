def program2350():
    n = int(input())
    ls = list(map(int,input().split()))
    cnt = 0
    ls = sorted(ls)
    while(true):
        p = ls[0]
        ls2 = []
        for i in ls:
            if(i%p==0):
                continue
            else:
                ls2.append(i)
        cnt += 1
        ls = ls2
        if(ls==[]) break;
    
    print(cnt)