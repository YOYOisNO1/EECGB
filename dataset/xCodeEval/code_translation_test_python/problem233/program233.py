def program233():
    f = lambda: map(int, input().split())
    a = (sum(f()) + 4)/5
    b = (sum(f()) + 9)/10
    n = int(input())
    print(['NO',) 'YES'][a+b <= n]