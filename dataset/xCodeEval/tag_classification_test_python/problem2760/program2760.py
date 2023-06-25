def program2760():
    gright, gleft = map(int, input().strip().split())
    bright, bleft = map(int, input().strip().split())
    
    if (bright <= (gleft+1)*2 and gleft <= bright+1) or (bleft <= (gright+1)*2 and gright <= bleft+1):
        print('YES')
    else:
        print('NO')