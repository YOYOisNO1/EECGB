def program4245():
    p1=list(map(int,input().split()))
    p2=list(map(int,input().split()))
    if(p1[0]!=p2[0] and p1[1]!=p2[1]):
        ans=2*(abs(p1[0]-p2[0])+1)+2*(abs(p1[1]-p2[1])+1)
    elif(p1[0]!=p2[0] and p1[1]==p2[1]):
        ans=2*(abs(p1[0]-p2[0])+1)+4
    else:
        ans=ans=2*(abs(p1[1]-p2[1])+1)+4
    print(ans)
        