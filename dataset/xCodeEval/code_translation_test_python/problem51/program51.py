def program51():
    n   = int(input())
    xl  = list(map(int,input().split()))
    yl  = list(map(int,input().split()))
    print('Yes' if sum(xl)>=sum(yl) else 'No')
    