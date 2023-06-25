def program3365():
    a=int(input())
    if a==1:
        print(1)
        exit()
    cnt = 1
    for i in range(2,int(a**.5)+1):
        if a%i==0:
            cnt+=1
    cnt*=2
    if int(a**.5)**2 == a:
        cnt -= 1
    print(cnt)