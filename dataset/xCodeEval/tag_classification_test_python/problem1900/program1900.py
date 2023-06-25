    import sys
    
def check(arr,s,ind):
        # print(s)
        
        if(s%360==0 and ind==15):
            # print(s)
            print("YES")
            exit(0)
        if(ind>=15):
            return
        check(arr,s+arr[ind],ind+1)
        check(arr,s-arr[ind],ind+1)
        
    n=int(sys.stdin.readline())
    # print(n)
    
    ip=[]
    for i in range(n):
        a=int(sys.stdin.readline())
        ip.append(a)
    for i in range(n,15):
        ip.append(0)
    
    # print(ip)
    
    check(ip,0,0)
    print("NO")