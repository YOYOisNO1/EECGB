def program3963():
    x1,y1,x2,y2 = mp(int,input().split());
    n = x2 - x1;
    m = n/2 + 1;
    n /= 2;
    h = y2 - y1 - 1;
    print h*m + (h - 1)*n;