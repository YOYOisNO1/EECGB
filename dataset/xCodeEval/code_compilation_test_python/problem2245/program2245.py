def program2245():
        inp = input().split(' ')
        inp = list(map(int,inp))
        x1 = int(inp[0])
        y1 = int(inp[1])
        x2 = int(inp[2])
        y2 = int(inp[3])
        tinp = input().split(' ')
        tinp = list(map(int,tinp))
        tx = int(tinp[0])
        ty = int(tinp[1])
        if (((((x2-x1)//tx)%2==0)and(((y2-y1)//ty)%2==0))or((((x2-x1)//tx)%2!=0)and(((y2-y1)//ty)%2!=0))):
            print('YES')
        else:
            print('NO')