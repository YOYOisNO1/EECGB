    from math import *
    
def checkInt(f):
        if abs(int(f+0.0001)-f)<=0.001:
            return True
        else:
            return False
    
    p1 = input()
    p1x,p1y = p1.split(' ')
    p2 = input()
    p2x,p2y = p2.split(' ')
    p3 = input()
    p3x,p3y = p3.split(' ')
    p1x = float(p1x)
    p1y = float(p1y)
    p2x = float(p2x)
    p2y = float(p2y)
    p3x = float(p3x)
    p3y = float(p3y)
    dis12 = sqrt((p1x-p2x)**2+(p1y-p2y)**2)
    dis23 = sqrt((p2x-p3x)**2+(p2y-p3y)**2)
    dis13 = sqrt((p1x-p3x)**2+(p1y-p3y)**2)
    cent12x = 0.5*(p1x+p2x)
    cent12y = 0.5*(p1y+p2y)
    cent13x = 0.5*(p1x+p3x)
    cent13y = 0.5*(p1y+p3y)
    cent23x = 0.5*(p2x+p3x)
    cent23y = 0.5*(p2y+p3y)
    k12 = (p2y-p1y+0.000000001)/(p2x-p1x+0.000000001)
    k13 = (p3y-p1y+0.000000001)/(p3x-p1x+0.000000001)
    k23 = (p2y-p3y+0.000000001)/(p2x-p3x+0.000000001)
    k12op = -1/k12
    k13op = -1/k13
    k23op = -1/k23
    b12 = -k12op*cent12x+cent12y
    b13 = -k13op*cent13x+cent13y
    b23 = -k23op*cent23x+cent23y
    centx = (b13-b12)/(k12op-k13op)
    centy = k12op*centx + b12
    radius = sqrt((centx-p1x)**2+(centy-p1y)**2)
    if 0.5*dis12/radius>1:
        theta1 = 2*asin(1)
    else:
        theta1 = 2*asin(0.5*dis12/radius)
    if 0.5*dis13/radius>1:
        theta2 = 2*asin(1)
    else:
        theta2 = 2*asin(0.5*dis13/radius)
    
    if 0.5*dis23/radius>1:
        theta3 = 2*asin(1)
    else:
        theta3 = 2*asin(0.5*dis23/radius)
    minimumside = 0
    theta = 0
    side = 2
    while (True):
        side += 1
        calctheta = 2*pi/side
        if (checkInt(theta1/calctheta) and checkInt(theta2/calctheta) and checkInt(theta3/calctheta)):
            minimumside = side
            theta = calctheta/2
            break
    halfsidel = sin(theta)*radius
    h = cos(theta)*radius
    s = minimumside*h*halfsidel
    print(s)