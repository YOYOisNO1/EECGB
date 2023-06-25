def program2387():
    import sys
    n = input().strip()
    
    if int(n[0]) > 1:
        print( 2 ** len(n) - 1 )
    else:
        lenn = len(n)
        x = 2 ** (lenn-1) - 1
        for i in range(1, lenn):
            if int(n[i]) > 1:
                x += 2 ** (lenn - i)
                print(x)
                sys.exit(0)
            elif int(n[i]) == 1:
                x += 2 ** (lenn - 1 - i)
            else:
                continue
        print(x+1)