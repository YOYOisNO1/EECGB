def program999():
    # cook your dish here
    # your code goes here
    n,a= input().split()
    n=int(n)
    a=int(a)
    arr=[int(x) for x in input().split()]
    count=0
    
    point1=a-1
    point2=a+1
    if arr[a]==1:
        count+=1
    
    for i in range(0,len(arr)):
        if point1<0 and point2<len(arr):
            if arr[point2]==1:
                count+=1
            point2+=1
        elif point1>=0 and point2>len(arr)-1:
            if arr[point1]==1:
                count+=1
            point1-=1
        elif point1>=0 and point2<=len(arr)-1:
            if arr[point1]==1 and arr[point2]==1:
                count+=2
            point1-=1
            point2+=1
        else:
            break
        
     print(count)
        
            
            
        