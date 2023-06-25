def program1887():
    import math
    m,n=map(int,input().split( ))
    if n<=math.ceil(m/2):
        print(int(n*2 - 1))
    else:
        print(2*(n-math.ceil(m/2)))