def program3691():
    a,b,r = map(int, input().split())
    print("First") if r*2<=a and r*2<=b else "Second"