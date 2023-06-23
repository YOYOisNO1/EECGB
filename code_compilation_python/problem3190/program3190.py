def isCovered(p1, p2, p3, p4, p5, p6):
        x1,y1 = p1 #cp bottom left
        x2,y2 = p2 #cp top right
        x3,y3 = p3 #t1 bottom left
        x4,y4 = p4 #t1 top right
        x5,y5 = p5 #t2 bottom left
        x6,y6 = p6 #t2 top right
    
        if (x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2) or (x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2):
            return "COMPLETELY COVERED"
        elif y5 <= y1 <= y2 <= y6 and y3 <= y1 <= y2 <= y4 and x5 <= x1 < x6 and x3 <= x2 < x4 and (x6-x1+x2-x3) >= (x2-x1):
            return "COMPLETELY COVERED"
        elif x5 <= x1 <= x2 <= x6 and x3 <= x1 <= x2 <= x4 and y5 <= y1 < y6 and y3 <= y2 < y4 and (y6-y1+y2-y3) >= (y2-y1):
            return "COMPLETELY COVERED"
        elif y5 <= y1 <= y2 <= y6 and y3 <= y1 <= y2 <= y4 and x3 <= x1 < x4 and x5 <= x2 < x6 and (x4-x1+x2-x5) >= (x2-x1):
            return "COMPLETELY COVERED"
        elif x5 <= x1 <= x2 <= x6 and x3 <= x1 <= x2 <= x4 and y3 <= y1 < y4 and y5 <= y2 < y6 and (y4-y1+y2-y5) >= (y2-y1):
            return "COMPLETELY COVERED"
        else:
            return "NOT COMPLETELY COVERED"
    
    first=map(int,input().split())
    second=map(int,input().split())
    third=map(int,input().split())
    p1=(first[0],first[1])
    p2=(first[2],first[3])
    p3=(second[0],second[1])
    p4=(second[2],second[3])
    p5=(third[0],third[1])
    p6=(third[2],third[3])
    if(isCovered(p1,p2,p3,p4,p5,p6)=="CMPLETELY COVERED")
        print("YES")
    else:
        print("NO")