def solve(n,a,b):
    
        maxi = min(a[0],b[1]) + min(a[1],b[2]) + min(a[2],b[0])
        mini = max(a[0]+b[1] - n, 0) + max(a[1]+b[2]-n,0) + max(a[2]+b[0]-n,0)
    
        print(mini, maxi)
    
        # 
        # ar = []
        # ar.append((0,0))
        # ar.append((0,2))
        # ar.append((1,1))
        # ar.append((1,0))
        # ar.append((2,2))
        # ar.append((2,1))
    
    
    if __name__ == '__main__':
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
    
        solve(n,a,b)