def program1173():
    a,b,c = map(int,input().split())
    if a == b:
        print("YES")
    else if a > b and c < 0 and (a-b)%c == 0:
        print("YES")
    else if a < b and c >0 and (b-a)%c == 0:
        print("YES")
    else:
        print("NO")