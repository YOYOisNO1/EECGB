def program2284():
    f = input()
    t1 = 0
    t2 = 0
    for k in f:
        if k=='1' and t2<7:
            t1+=1
            t2 = 0
        elif k=='0' and t1<7:
            t2+=1
            t1 = 0
    if t2>=7 or t1>=7:
        print('YES')
    else:
        print("NO")