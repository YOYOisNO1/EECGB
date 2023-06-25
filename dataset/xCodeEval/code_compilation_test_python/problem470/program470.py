def program470():
    k,r=map(int,input().split());i=1
    while (i*k%10!=0) & (i*k%10!=r):i++
    print(i)