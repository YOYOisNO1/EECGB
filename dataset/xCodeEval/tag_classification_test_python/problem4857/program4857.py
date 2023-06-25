    import sys
def fastio():
        from io import StringIO
        from atexit import register
        global input
        sys.stdin = StringIO(sys.stdin.read())
        input = lambda : sys.stdin.readline().rstrip('\r\n')
        sys.stdout = StringIO()
        register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
    fastio()
     
def debug(*var, sep = ' ', end = '\n'):
        print(*var, file=sys.stderr, end = end, sep = sep)
     
    INF = 10**20	
    MOD = 10**9 + 7
    I = lambda:list(map(int,input().split()))
    
    a,b = list(map(int , input().split()))
    if(a<b): print(0)
    else:
        if a==b:
            print('infinity')
        elif a>b:
            cnt =0
            for i in range(1,int((a-b)**0.5)+1):
                if(a-b)%i==0:
                    if(i>b): cnt+=1
                    if(a-b)/i > b and i*i != (a-b) : cnt+=1
            
            print(cnt)