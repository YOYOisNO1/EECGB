def program2552():
    a, b, c = map(int, input().split())
    ok = False
    for i in range(c//a+1):
        #print(c-a*i)
        #print((c-a*i)%b==0)
        if c-a*i >= 0 and (c-a*i)%b==0:
            ok = True
    if ok:
        print("Yes")
    else:
        print("No")