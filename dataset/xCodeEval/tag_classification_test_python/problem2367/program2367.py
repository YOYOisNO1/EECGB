def program2367():
    n,w=map(int,input().split())
    l=list(map(int,input().split()))
    Half=[(i+1)//2 for i in l]
    pos=[[l[i],(l[i]+1)//2,i] for i in range(n)]
    pos.sort(reverse=True)
    if w<sum(Half):
        print(-1)
        quit()
    extra=w-sum(Half)
    #print(extra)
    for i in range(n):
        if extra>0:
            rem=pos[i][0]-pos[i][1]
            if rem>=extra:
                Half[pos[i][2]]+=extra
                extra=0
                break
            else:
                extra-=rem
                Half[pos[i][2]]=pos[i][0]
    print(*Half)