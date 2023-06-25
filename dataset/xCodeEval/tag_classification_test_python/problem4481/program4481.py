def program4481():
    from math import ceil,pow
    n=int(input())
    x=ceil(round(pow(n,0.1)*10,4))
    s='codeforces'
    z=x//10
    p=1
    for i in range(10):
        if i<x%10:
            print(s[i]*(z+1),end='')
            p*=(z+1)
        else:
            print(s[i]*z,end='')
            p*=z
    i=0
    while (p//z)*(z+i)<n:
        i+=1
    print('s'*i,end='')