def program325():
    import math
    days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    m,d=map(int,input().split())
    ans=math.ceil((days[m]-8+ d)/7)+1
    print(ans)