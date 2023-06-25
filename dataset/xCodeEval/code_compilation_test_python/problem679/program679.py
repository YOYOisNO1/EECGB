def program679():
    n,mex=map(int,input().split())
    steps=0
    flag=True
    nums=map(int,input().split())
    if mex==0 and nums[0]==0:
        print 1
        flag=False
    while True and flag:
        nuMex=0
        for i in range(100):
            if i not in nums:
                nuMex=i
                break
        if nuMex>mex:
            nums.remove(nuMex)
            steps+=1
        elif nuMex<mex:
            nums.append(nuMex)
            nums.sort()
            steps+=1
        else:
            print steps
            break
        
        