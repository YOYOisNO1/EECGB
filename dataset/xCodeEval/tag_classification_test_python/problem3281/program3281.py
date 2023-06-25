def program3281():
    n = int(input())
    a = map(int,input().split())
    a.insert(0,0)
    a.append(999)
    ans = 0
    start = a[0]
    
    for event in a:
        if(event - start > 15):
            ans = start+15
            break
        start = event
    print(min(90,ans))