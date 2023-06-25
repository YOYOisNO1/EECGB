def solve():
        nn=input().split(' ')
        n=int(nn[0])
        x=int(nn[1])
        queue=[]
        queue.append(x)
        vis=set()
        vis.add(x)
        ans=0
        while len(queue)>0:
            s=len(queue)
            while s>0:
                t=queue.pop(0)
                if len(str(t))==n:
                    print(ans)
                    return -1
                for j in str(t):
                    cc= t*int(j)
                    if cc not in vis:
                        queue.append(cc)
                        vis.add(cc)
                s-=1
            ans+=1
        print(-1)
        return -1
    
    solve()