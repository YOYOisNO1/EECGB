def program1381():
    a,b = map(int,input().split());cnt = 0
    for i in range(1,a+1):
        cnt+=(b+(i%5))//5
    print(cnt)