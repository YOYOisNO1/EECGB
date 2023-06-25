def program4341():
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    flag = 1
    if(b==d):
        print(b)
        flag = 0
    else:
        for i in range(100):
            for j in range(100):
                if b+(i*a)==d+(j*c):
                    print(b+(i*a))
                    flag = 0
                    break
            if not flag:
                break
    if flag:
        print(-1)
        