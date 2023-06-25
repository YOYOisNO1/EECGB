def program1198():
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt1 = 0
    cnt2 = 0
    
    
    for i in range(n):
        if a[i] > b[i]:
            cnt1 += 1
        if a[i] < b[i]:
            cnt2 += 1
    
    if(cnt1 > cnt2):
        print(1)
        exit(0)
    if cnt1 == 0:
        print('-1')
        exit(0)
    
    print(int((cnt2 / cnt1 + 1)))