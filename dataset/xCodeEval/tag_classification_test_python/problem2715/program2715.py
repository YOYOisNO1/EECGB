def program2715():
    x,y=map(int,input().split())
    t=0
    while True:
        if t%2==0:
            if x>=2 and y>=2:
                x-=2;y-=2
            elif x==1 and y>=12:
                x-=1;y-=12
            elif x==0 and y>=22:
                y-=22
            else:exit(print('Hanako'))
        else:
            if y>=22:
                y-=22
            elif x>=1 and y>=12:
                y-=12;x-=1
            elif x>=2 and y>=2:
                x-=2;y-=2
            else:exit(print('Ciel'))
        t+=1