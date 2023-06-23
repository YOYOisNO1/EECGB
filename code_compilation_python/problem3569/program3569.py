    #._.
    #want to maximize xa+y*int((c-z*a)/w)
    
def maxi(c, x, y, z, w):
        one = x / z
        two = y / w
        dictx = {}
    def f(a):
            return x*a+y*int((c-z*a)/w)
        for a in range(0, int(c//w)+1):
            dictx[a] = f(a)
        
        return max(dictx, key = lambda x:dictx[x])
    c, x, y, z, w = list(map(int, input().split(' ')))
    bad = maxi(c, x, y, z, w)
    print(x*bad+y*int((c-z*bad)/w))