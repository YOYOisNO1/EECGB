def GetMaxDiff(arr,i):
        max_diff=0
        arr1=arr[:i]+arr[i+1:]
        for j in range(len(arr1)-1):
            diff = int(arr1[j+1])-int(arr1[j])
            #print(diff)
            if diff>max_diff:
                max_diff=diff
        return max_diff
    
    n = int(input())
    hangs = input().split()
    min_diff=int(hangs[n-1])-int(hangs[0])
    
    for i in range(1,n-1):
        max_diff = GetMaxDiff(hangs,i)
        #print(max_diff)
        if max_diff<min_diff:
            min_diff=max_diff
    
    print(min_diff)