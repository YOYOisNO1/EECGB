def program1735():
    l,r,x,y,k=map(int,input().split())
    l+=k-1
    l//=k
    r//=k
    print("NO"if l>r or x>r or l>y else"YES")