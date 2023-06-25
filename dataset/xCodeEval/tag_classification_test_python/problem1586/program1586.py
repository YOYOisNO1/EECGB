def program1586():
    a,b=map(int,input().split())
    if abs(a-b)>1 :
        print("NO")
    elif a==0 and b==0:
        print("NO")
    else:
        print("YES")