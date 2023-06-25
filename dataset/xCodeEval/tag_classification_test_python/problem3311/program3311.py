def program3311():
    n,m,r=map(int,input().split())
    li=list(map(int,input().split()))
    li1=list(map(int,input().split()))
    print(max(r,(r//min(li)*max(li1)+r%min(li))))