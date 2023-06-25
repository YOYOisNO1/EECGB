def program351():
    n = int(input())
    m=int(n/10000)*10000+int(n/100)%10*1000+n%10*100+int(n/10)%10*10+int(n/1000)%10
    ans = 1
    for i in range(5):
        ans=int(ans*m%100000)
    print("{:05d}".format(ans))