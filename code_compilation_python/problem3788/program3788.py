def program3788():
    n = input()
    x, y = map(int, input().split())
    if x + y <= n + 1:
        print "White"
    else:
        print "Black"