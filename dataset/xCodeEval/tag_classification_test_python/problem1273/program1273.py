    class point:
        x=0
        y=0
    
    def __init__(self,x,y):
            self.x=x
            self.y=y
    
    def __cmp__(self, b):
            if(self.cmp(b)):
                return -1
            elif b.cmp(self):
                return 1
            else:
                return 0
    
    def cmp(self, b):
            if (self.x == b.x):
                return self.y < b.y
            return self.x < b.x
    
    def printf(self):
            return self.x,self.y
    
def judge(a,b):
        return a.x*b.y==a.y*b.x
    
def dis(a,b):
        x=a.x*a.x+a.y*a.y
        y=b.x*b.x+b.y*b.y
        return x==y
    
    ax,ay,bx,by,cx,cy=map(int,input().split())
    A=[]
    A.append(point(ax,ay))
    A.append(point(bx,by))
    A.append(point(cx,cy))
    B=point(A[1].x-A[0].x,A[1].y-A[0].y)
    C=point(A[2].x-A[1].x,A[2].y-A[1].y)
    if (not judge(B,C)) and dis(B,C):
        print('Yes')
    else:
        print('No')