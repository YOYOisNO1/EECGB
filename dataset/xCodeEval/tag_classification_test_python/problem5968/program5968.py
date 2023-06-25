def program5968():
    n=int(input())
    p=n//1234567+1
    for a in range(p):
        q=(n-a*1234567)//123456+1
        for b in range(q):
            r=n-a*1234567-b*123456
    
            if r%1234 ==0:
                print('YES')
                exit()
    else:
        print('NO')
    