def program433():
    import math
    a1,a2,a3 = input().split(" ")
    b1,b2,b3 = input().split(" ")
    n = int(input())
    a = int(a1)+int(a2)+int(a3)
    b = int(b1)+int(b2)+int(b3)
    if(math.ceil(a/5)+math.ceil(b/10) <= n):
        print("YES")
    else:
        print("NO")