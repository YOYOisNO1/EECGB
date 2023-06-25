def program1498():
    # brute force motherfuckers
    hopScotch = [1]
    for x in range(1,1000001,3):
        hopScotch.append(x+1)
        hopScotch.append([x+2,x+3])
    a,x,y = map(int,input().split())
    if y == 0 or abs(x) >= a: print(-1)
    else:
        seq = [1,2]
        jump,rem = y//a,y%a
        if rem + jump == jump: print(-1)
        else:
            if jump == 0:
                print((1) if abs(x) < a/2 else -1)
            else:
                match = seq[(jump+1)%2]
                if match == 1:
                    print(hopScotch[jump] if abs(x) < a/2 else -1)
                else:
                    if x == 0: print(-1)
                    else: print(hopScotch[jump][0] if x < 0 else hopScotch[jump][1])
    