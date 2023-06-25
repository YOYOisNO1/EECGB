def program7539():
    n,m,k=map(int, input().split())
    if n&1 == 0: print("Marsel")
    else:
        flag = False
        d=1
        while d*d <= m:
            if m%d == 0 and ((m>d and d>=k) or (d>1 and m/d>=k)):
                print("Timur")
                exit()
            d+=1
        print("Marsel")