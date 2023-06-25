def program4911():
    n=int(input())
    arr=list(map(int,input().split()))
    c=sum(arr[::3])
    b=sum(arr[1::3])
    ba=sum(arr[2::3])
    res=max(c,b,ba)
    if res==c:
        print("chest")
    elif res==b:
        print("biceps")
    else:
        print("back")