def program1957():
    n = input()
    a = input()
    b = input()
    ans = "NO"
    x = 0
    while x*a <= n:
        if (n-x*a)%b==0:
            ans = "YES"
            y = (n-x*a)/b
            break
        x+=1
    if ans=="YES":
        print(ans)
        print(x,y)
    else:
        print(ans)