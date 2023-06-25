def program4003():
    w,m=map(int,input().split())
    for i in range(33):
        if m>abs(w**(32-i)-m):
            m=abs(w**(32-i)-m)
    if m==0:
        print("YES")
    else:
        print("NO")