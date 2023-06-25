def program2885():
    n=int(input())
    
    
    s=input()
    arr=[0]*n
    for i in range(len(s)):
        if s[len(s)-i-1]=='B':
            arr[i]=1
    print(arr)
    count=0
    b=True
    while True:
        index=0
        for i in range(n-1,-1,-1):
            if arr[i]==1:
                index=i
                break
            if i==0:
                b=False
        if not b:
            break
        arr[index]=0
        for i in range(index+1,n):
            arr[i]=1
        print(arr)
        count+=1
    
    print(count)