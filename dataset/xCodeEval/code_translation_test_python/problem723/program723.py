def program723():
    n = int(input())
    arr =  list(map(int,input().split()))
    arr.sort()
    minIns = 0
    for k in range(len(arr)-1):
        minIns+=arr[k+1]-arr[k]
    for i in range(0,2*n):
        for j in range(i+1,2*n):
            newArr = arr[0:i]+arr[i+1:j]+arr[j+1:]
            #print(i,j,newArr)
            #Ins = 0
            
            minIns=min(minIns,sum(newArr[k+1]-newArr[k] for k in range(0,len(newArr)-1,2)))
    
    print(minIns)