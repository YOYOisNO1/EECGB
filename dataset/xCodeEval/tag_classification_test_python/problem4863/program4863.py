    class Point:
        x=None 
        y=None 
    def __init__(self,x,y):
            self.x=x 
            self.y=y 
        
def onSegment(p,q,r):
        if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
           return True
        return False
     
def orientation(p,q,r):
        val=(q.y-p.y)*(r.x-q.x)-(q.x-p.x)*(r.y-q.y)
        if val == 0:
            return 0
        if val>0:
            return 1
        return 2
    
def doIntersect(p1,q1,p2,q2):
        o1=orientation(p1,q1,p2)
        o2=orientation(p1,q1,q2)
        o3=orientation(p2,q2,p1)
        o4=orientation(p2,q2,q1)
        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and onSegment(p1, p2, q1): 
            return True
        if o2 == 0 and onSegment(p1, q2, q1): 
            return True
        if o3 == 0 and onSegment(p2, p1, q2): 
            return True
        if o4 == 0 and onSegment(p2, q1, q2): 
            return True
        return False
        
def arrange(arr,n):
        p1=arr[0:2]
        p2=arr[2:4]
        p3=arr[4:6]
        p4=arr[6:8]
        aaa=[p1,p2,p3,p4]
        aaa.sort()
        if n==1:
            arr1=[aaa[0][0],aaa[0][1],aaa[2][0],aaa[2][1],aaa[3][0],aaa[3][1],aaa[1][0],aaa[1][1]]
        else:
            arr1=[aaa[0][0],aaa[0][1],aaa[1][0],aaa[1][1],aaa[3][0],aaa[3][1],aaa[2][0],aaa[2][1]]
        return arr1
        
def isInside(polygon,n,p):
        if n<3:
            return False
        extreme=Point(10**100,p.y)
        count=0
        start=0
        i=0 
        while i!=0 or start==0:
            start=1
            nextt=(i+1)%n
            if (doIntersect(polygon[i], polygon[nextt], p, extreme)):
                if (orientation(polygon[i], p, polygon[nextt])==0):
                   return onSegment(polygon[i], p, polygon[nextt])
                count+=1
            i=nextt
        return bool(count&1); 
    
    arr=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    arr=arrange(arr,1)
    arr1=arrange(arr1,2)
    #print(arr,arr1)
    flag=0
    i=0
    while i<8:
        p1=Point(arr[i],arr[i+1])
        q1=Point(arr[(i+2)%8],arr[(i+3)%8])
        j=0
        while j<8:
            p2=Point(arr1[j],arr1[j+1])
            q2=Point(arr1[(j+2)%8],arr1[(j+3)%8])
            #print(p1.x,p1.y,q1.x,q1.y,"      ",p2.x,p2.y,q2.x,q2.y)
            if doIntersect(p1, q1, p2, q2):
                flag=1
            j+=2
        i+=2
    arr2=[Point(arr[0],arr[1]),Point(arr[2],arr[3]),Point(arr[4],arr[5]),Point(arr[6],arr[7])]
    arr3=[Point(arr1[0],arr1[1]),Point(arr1[2],arr1[3]),Point(arr1[4],arr1[5]),Point(arr1[6],arr1[7])]
    if flag==1 or (isInside(arr3,4,Point(arr[0],arr[1])) and isInside(arr3,4,Point(arr[2],arr[3])) and isInside(arr3,4,Point(arr[4],arr[5])) and isInside(arr3,4,Point(arr[6],arr[7]))) or (isInside(arr2,4,Point(arr1[0],arr1[1])) and isInside(arr2,4,Point(arr1[2],arr1[3])) and isInside(arr2,4,Point(arr1[4],arr1[5])) and isInside(arr2,4,Point(arr1[6],arr1[7]))):
        print("Yes")
    else:
        print("No")
    #print(flag==1 , (isInside(arr3,4,Point(arr[0],arr[1])) and isInside(arr3,4,Point(arr[2],arr[3])) and isInside(arr3,4,Point(arr[4],arr[5])) and isInside(arr3,4,Point(arr[6],arr[7]))) , (isInside(arr2,4,Point(arr1[0],arr1[1])) and isInside(arr2,4,Point(arr1[2],arr1[3])) and isInside(arr2,4,Point(arr1[4],arr1[5])) and isInside(arr2,4,Point(arr1[6],arr1[7]))))