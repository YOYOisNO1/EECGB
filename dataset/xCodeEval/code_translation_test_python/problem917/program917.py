def program917():
    h,m,i=map(int,input().split(':'))+[0]
    while h/10!=m%10 or h%10!=m/10:
        h,m,i=(h+(m==59))%24,(m+1)%60,i+1
    print(i)