    # -*- coding: utf-8 -*-
    """
    Created on Thu Jul 16 07:38:09 2020
    
    @author: Dark Soul
    """
    
def squar(x1,y1,x2,y2,x3,y3,x4,y4):
        ar=(x1*y2+x2*y3+x3*y4+x4*y1-x2*y1-x3*y2-x4*y3-x1*y4)/2
        return abs(ar)
def line(x1,y1,x2,y2):
        if x1-x2==0:
            return ['c',x1]
        else:
            m=(y1-y2)/(x1-x2)
            c=y1-(x1*(y1-y2)/(x1-x2))
            return [m,c]
def triangl(x1,y1,x2,y2,x3,y3):
        ar=(x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)/2
        return abs(ar)
def isinside(x1,y1,x3,y3,x5,y5):
        if (x5>=x1 and x5<=x3) and (y5>=y1 and y5<=y3):
            return 1
        else:
            return 0
        
    co1=list(map(int, input().split()))
    co2=list(map(int, input().split()))
    x1=co1[0]
    y1=co1[1]
    x2=co1[2]
    y2=co1[3]
    x3=co1[4]
    y3=co1[5]
    x4=co1[6]
    y4=co1[7]
    x5=co2[0]
    y5=co2[1]
    x6=co2[2]
    y6=co2[3]
    x7=co2[4]
    y7=co2[5]
    x8=co2[6]
    y8=co2[7]
    
    xin=[x1,x2,x3,x4,x1]
    yin=[y1,y2,y3,y4,y1]
    xout=[x5,x6,x7,x8,x5]
    yout=[y5,y6,y7,y8,y5]
    
    
    xmin=min(x1,x2,x3,x4)
    ymin=min(y1,y2,y3,y4)
    xmax=max(x1,x2,x3,x4)
    ymax=max(y1,y2,y3,y4)
    
    inx=sorted([x1,x2,x3,x3])
    iny=sorted([y1,y2,y3,y4])
    
    sq1=squar(x1,y1,x2,y2,x3,y3,x4,y4)
    sq2=squar(x5,y5,x6,y6,x7,y7,x8,y8)
    
    sign=0
    flag=0
    
    xo=[x5,x6,x7,x8,x5]
    yo=[y5,y6,y7,y8,y5]
    xi=[x1,x2,x3,x4]
    yi=[y1,y2,y3,y4]
    trsum=0
    
    for j in range(4):
        trsum=0
        for i in range(4):
            trsum=trsum+triangl(xo[i],yo[i],xo[i+1],yo[i+1],xi[j],yi[j])
        if abs(sq2-trsum)<=0.001:
            sign=1
            
        
    m=[0,0,0,0]
    c=[0,0,0,0]
    
    [m[0],c[0]]=line(x5,y5,x6,y6)
    [m[1],c[1]]=line(x6,y6,x7,y7)
    [m[2],c[2]]=line(x7,y7,x8,y8)
    [m[3],c[3]]=line(x8,y8,x5,y5)
    
    outx=sorted([x5,x6,x7,x8,x5])
    outy=sorted([y5,y6,y7,y8,y5])
    
    if isinside(xmin,ymin,xmax,ymax,x5,y5) or isinside(xmin,ymin,xmax,ymax,x6,y6) or isinside(xmin,ymin,xmax,ymax,x7,y7) or isinside(xmin,ymin,xmax,ymax,x8,y8):
        flag=1
        
    elif sign==1:
        flag=1
    else:
        flag=0
        for i in range(4):
            [m[i],c[i]]=line(xout[i],yout[i],xout[i+1],yout[i+1])
            for j in range(4):
                [a,b]=line(xin[j],yin[j],xin[j+1],yin[j+1])
                if a==0:
                    xx=(b-c[i])/m[i]
                    if xx<=inx[3] and xx>=inx[0] and xx<=max(xout[i],xout[i+1]) and xx>=min(xout[i],xout[i+1]) and b<=max(yout[i],yout[i+1]) and b>=min(yout[i],yout[i+1]):
                    
                        flag=1
                        break
                else:
                    yy=b*m[i]+c[i]
                    if yy>=iny[0] and yy<=iny[3] and yy<=max(yout[i],yout[i+1]) and yy>=min(yout[i],yout[i+1]) and b<=max(xout[i],xout[i+1]) and b>=min(xout[i],xout[i+1]):
                    
                        flag=1
                        break
            if flag:
                  break
            
    if flag:
        print('YES')
    else:
        print('NO')