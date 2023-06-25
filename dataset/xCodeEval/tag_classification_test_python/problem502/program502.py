def program502():
    *a,x=map(int,input().split())
    x+=1
    y=x//2
    c=2
    if x%2:
     c=a[0]<a[1];a[c]-=1
    s='0'*(a[0]-y)+'01'*y+'1'*(a[1]-y)
    print((s+'0','1'+s,s)[c])