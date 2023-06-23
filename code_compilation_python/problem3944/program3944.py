    import sys, os
    
    if os.environ['USERNAME']=='kissz':
        inp=open('in.txt','r').readline
    def debug(*args):
            print(*args,file=sys.stderr)
    else:
        inp=sys.stdin.readline    
    def debug(*args):
            pass
    
    # SCRIPT STARTS HERE
    
    h,w=map(int,inp().split())
    M=[]
    for _ in range(h):
        M+=[inp().strip()]
    
    x=y=0
    cnt=0
    Q=[(x,y)]
    while (x<h-1 or y<w-1):
        while Q:
            x,y=Q.pop(0)
            if M[x][y]=='*' or (x>=h-1 and y>=w-1): break
            if y<w-1:
                Q.append((x,y+1))
            if x<h-1:
                Q.append((x+1,y))
        cnt+=int(M[x][y]=='*')
        Q=[(x,y+1),(x+1,y)]
        #debug(Q)
    
            
    print(cnt)