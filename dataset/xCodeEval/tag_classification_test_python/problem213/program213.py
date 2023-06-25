def program213():
    x,y=map(int, input().split())
    n=int(input())
    m=1000000007
    func=[x,y,y-x,-x,-y,x-y]
    print(func[n%6-1]%m)