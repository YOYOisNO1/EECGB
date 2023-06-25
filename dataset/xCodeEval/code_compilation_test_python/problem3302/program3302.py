def program3302():
    #input
    n,m=map(int,input().split())
    nstr=str(input())
    mstr=str(input())
    
    #variables
    
    #main
    if '^' not in mstr or 'v' not in mstr:
    	print('NO')
    	quit()
    if '>' not in nstr or '<' not in nstr:
    	print('NO')
    	quit()
    if nstr[0]=='>' and mstr[0]=='v':
    	print('NO')
    	quit()
    if nstr[0]=='>' and mstr[-1]=='^':
    	print('NO')
    	quit()
    if nstr[-1]=='<' and mstr[0]=='v':
    	print('NO')
    	quit()
    if nstr[-1]=='<' and mstr[-1]=='^':
    	print('NO')
    	quit()
    print('YES')