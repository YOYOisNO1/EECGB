def program1061():
    n=int(input())
    a1,a2,a3=list(map(int,input().rstrip().split()))
    b1,b2,b3=list(map(int,input().rstrip().split()))
    ans=[0,0]
    ans[1]=min(a1,b2)+min(a2,b3)+min(a3,b1)
    ans[0]=max(0,b1-(a1+a2),b2-(a2+a3),b3-(a1+a3))
    print(*ans)