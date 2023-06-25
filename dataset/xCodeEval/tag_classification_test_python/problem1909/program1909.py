def program1909():
    h,m = map(int,input().split(":"));
    h %= 12;
    t = h*60 + m;
    t1 = 180*t/360.;
    t2 = m*6;
    print("%.10f %.10f")%(t1,t2);