def f(t,x):
        if t[1]-x<0:
            t[1]=t[1]-x+60
            t[0]=t[0]-1
            if t[0]<0:
                t[0]=t[0]+24
        else:
            t[1]=t[1]-x
        return t
def g(t):
        if '7' in (str(t[0])+str(t[1])):
            return True
        else:
            return False
    x = int(input())
    t = map(int,input().split())
    k = 0
    while True:
        if g(t):
            print(k)
            break
        else:
            t = f(t,x)
            k = k + 1