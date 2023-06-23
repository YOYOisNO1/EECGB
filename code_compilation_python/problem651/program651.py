def program651():
    s=input()
    a,b=input().split()
    x="6789TJQKA"if a[1]==s: print("YES")
    elif b[1]==s or a[1]!=b[1]: print("NO")
    elif x.index(a[0])>x.index(b[0]): print("YES")
    else: print("NO")