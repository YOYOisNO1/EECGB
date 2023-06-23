def program1188():
    from sys import *
    n=int(input())
    for i in range(n//1234567+1):
        for j in range(n//123456+1):
            t=i*1234567+j*123456
            if n-t>0 and (n-t)%1234==0: print('YES'); exit()
    print('NO')