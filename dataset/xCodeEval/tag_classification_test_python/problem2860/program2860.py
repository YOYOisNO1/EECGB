    import sys,math,string,bisect
    input=sys.stdin.readline
    from collections import deque,defaultdict
    L=lambda : list(map(int,input().split()))
    Ls=lambda : list(input().split())
    M=lambda : map(int,input().split())
    I=lambda :int(input())
def dist(a,b,c,d):
        return abs(c-a)**2+abs(d-b)**2
    
    x1,y1,x2,y2,x3,y3=M()
    p=[[x1,y1],[x2,y2],[x3,y3]]
    a=dist(x1,y1,x2,y2)
    b=dist(x2,y2,x3,y3)
    c=dist(x3,y3,x1,y1)
    l=[a,b,c]
    l.sort()
    if(l[0]+l[1]==l[2]):
        print("RIGHT")
        exit()
    else:
        for i in range(3):
            p[i][0]+=1
            x=[(p[0][0],p[0][1]),(p[1][0],p[1][1]),(p[2][0],p[2][1])]
            if(len(set(x))==3):
                a=dist(p[0][0],p[0][1],p[1][0],p[1][1])
                b=dist(p[1][0],p[1][1],p[2][0],p[2][1])
                c=dist(p[2][0],p[2][1],p[0][0],p[0][1])
                l=[a,b,c]
                l.sort()
                p[i][0]-=1
                if(l[0]+l[1]==l[2]):
                    print("ALMOST")
                    exit()
            else:
               p[i][0]-=1
            
            p[i][0]-=1
            x=[(p[0][0],p[0][1]),(p[1][0],p[1][1]),(p[2][0],p[2][1])]
            if(len(set(x))==3):
                a=dist(p[0][0],p[0][1],p[1][0],p[1][1])
                b=dist(p[1][0],p[1][1],p[2][0],p[2][1])
                c=dist(p[2][0],p[2][1],p[0][0],p[0][1])
                l=[a,b,c]
                l.sort()
                p[i][0]+=1
                if(l[0]+l[1]==l[2]):
                    print("ALMOST")
                    exit()
            else:
               p[i][0]+=1
            p[i][1]+=1
            x=[(p[0][0],p[0][1]),(p[1][0],p[1][1]),(p[2][0],p[2][1])]
            if(len(set(x))==3):
                a=dist(p[0][0],p[0][1],p[1][0],p[1][1])
                b=dist(p[1][0],p[1][1],p[2][0],p[2][1])
                c=dist(p[2][0],p[2][1],p[0][0],p[0][1])
                l=[a,b,c]
                l.sort()
                p[i][1]-=1
                if(l[0]+l[1]==l[2]):
                    print("ALMOST")
                    exit()
            else:
               p[i][1]-=1
            p[i][1]-=1
            x=[(p[0][0],p[0][1]),(p[1][0],p[1][1]),(p[2][0],p[2][1])]
            if(len(set(x))==3):
                a=dist(p[0][0],p[0][1],p[1][0],p[1][1])
                b=dist(p[1][0],p[1][1],p[2][0],p[2][1])
                c=dist(p[2][0],p[2][1],p[0][0],p[0][1])
                l=[a,b,c]
                l.sort()
                p[i][1]+=1
                if(l[0]+l[1]==l[2]):
                    print("ALMOST")
                    exit()
            else:
               p[i][1]+=1
    print("NEITHER")