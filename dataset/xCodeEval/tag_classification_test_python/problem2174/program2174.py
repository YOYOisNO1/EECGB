def program2174():
    x,y,z,t1,t2,t3=[int(i) for i  in input().split()]
    ele=(3*t3)+(abs(z-x)*t2)+(abs(y-x)*t2)
    sta=(abs(y-x)*t1)
    if(ele<=sta):
        print("YES")
    else:
        print("NO")