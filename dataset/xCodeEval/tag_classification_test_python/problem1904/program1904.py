def program1904():
    import sys
    a = sys.stdin.readline()
    # a = '10 5'
    a = a.strip().split()
    x = int(a[0])
    y = int(a[1])
    t = abs(x) + abs(y)
    
    if x > 0 and y > 0:
        print('{} {} {} {}').format('0', str(t), str(t), '0')
    elif x > 0 and y < 0:
        print(0,) -t, t, 0
    elif x < 0 and y < 0:
        print(-t,) 0, 0, -t
    else:
        print(-t,) 0, 0, t