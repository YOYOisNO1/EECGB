def program704():
    
    numbers={}
    cubes=[]
    n=int(input())
    for i in range(n):
        cubes.append(map(int,input().split()))
    
    for cube in cubes:
        for j in cube:
            numbers[j]=True
    if n>=2        
        for (a,b) in [(i,j) for i in range(3) for j in range(i+1,3)]:
            for k in cubes[a]:
                for l in cubes[b]:
                    numbers[k*10+l]=True
                    numbers[l*10+k]=True
    
    if n==3:
        for (a,b,c) in [(i,j,k) for i in range(3) for j in range(i+1,3) for k in range(j+1,3)]:
            for l in cubes[a]:
                for m in cubes[b]:
                    for n in cubes[c]:
                        numbers[l*100+m*10+n]=True
                        numbers[l*100+n*10+m]=True
                        numbers[m*100+l*10+n]=True
                        numbers[m*100+n*10+l]=True
                        numbers[n*100+l*10+m]=True
                        numbers[n*100+m*10+l]=True
    
    count=0
    curr=0
    for i in sorted(numbers.keys()):
        if i==curr+1:
            count+=1
            curr=i
    print count