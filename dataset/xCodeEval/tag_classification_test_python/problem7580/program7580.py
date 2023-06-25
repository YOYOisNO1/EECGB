def program7580():
    n, rider, cop = map(int, input().split())
    rider, cop = rider - 1, cop - 1
    if input().strip() == 'to head':
        cop_dir = -1
    else:
        cop_dir = 1
    for pos, ch in enumerate(input().strip()):
        #print(pos, ch, rider, cop, cop_dir)
        if ch == '1':
            rider = -1
        else:
            if cop_dir == -1 and rider < cop:
                rider = max(0, rider - 1)
            elif cop_dir == 1 and rider > cop:
                rider = min(n - 1, rider + 1)
        cop += cop_dir
        if cop == rider:
            print('Controller %d' % (pos + 1))
            import sys; sys.exit()
        if cop == 0:
            cop_dir = 1
        elif cop == n - 1:
            cop_dir = -1
        if ch == '1':
            if cop_dir == -1:
                if cop == n - 1:
                    rider = 0
                else:
                    rider = n - 1
            else:
                if cop == 0:
                    rider = n - 1
                else:
                    rider = 0
    print('Stowaway')