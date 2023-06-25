def program571():
    ri=lambda:map(int,input().split(' '))
    r,g,b=ri()
    x=min(r,g,b)
    r-=x; g-=x; b-=x;
    x += r//3 + g//3 b//3
    print(x)