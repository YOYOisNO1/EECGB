def program5856():
    a, b, c = map(int, input().strip().split())
    
    vid = (c*a + b-1)/b
    print(vid-c)