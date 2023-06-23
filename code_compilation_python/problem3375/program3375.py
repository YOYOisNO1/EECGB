    import sys
    read=lambda:sys.stdin.readline().rstrip()
    readi=lambda:int(sys.stdin.readline())
    writeln=lambda x:sys.stdout.write(str(x)+"\n")
    write=lambda x:sys.stdout.write(x)
    '''
    a - 한 변의 길이
    x, y = 돌을 던진 곳의 위치
    
    반드시 네모 안에 들어가야만 함
    경계에 걸쳐도 -1
    
    
    h = 5 (-a, 4a), (a, 5a)
    h = 4 (-a/2, 3a), (a/2, 4a)
    h = 3 (-a, 2a), (a, 3a)
    h = 2 (-a/2, a) (-a/2, 2a)
    h = 1 :(-a/2, 0) (a/2, 0)
    
    h = 1 
        (-a/2, 0),(a/2, 1*a)
    h = 2K + 1 ( K = 1, 2, 3, ...)
        (-a, (h-1)*a), (a, h*a) 
    h = 2K
        (-a/2, h-1), (a/2, h)
    
    ha - ha + a
    '''
def solve(a,x,y):
        if not y % a:
            return -1
        if abs(x) >= a:
            return -1
        if y < a:
            if -a/2.0 < x < a/2.0:
                return 1
            else:
                return -1
    
    
    
        h = y // a
        if not h % 2:
            if x == 0:
                return -1
            if -a < x < 0:
                return 3*h//2 
            if 0 < x < a:
                return (3*h//2) + 1
            else:
                return -1   
        else:
            if -a/2.0 < x < a/2.0:
                return 3*((h+1)//2) - 1
            else:
                return -1
    
    A,X,Y=map(int, read().split())
    writeln(solve(A,X,Y))
    
    '''
    h = 1 2 3(h+1)/2 -1
    h = 3 5 
    h = 5 8
    
    h = 2 3 3(h//2)
    h = 4 6
    h = 6 9
    
    '''