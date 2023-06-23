def program3012():
    w,m=map(int,input().split())
    while m:
     if 1<m%w<m-1: break
     m=(m+1)%w
    print("NO" 1<m%w<m-1 else "YES") 