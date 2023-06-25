    a,b,n = [int(x) for x in input().split()]
def hcf(x,y):
        s = 0
        for i in range(1,min(x,y)+1):
            if x%i == 0 and y%i == 0:
                s = i
        return s
    s = 0
    t = a
    while n>max(hcf(t,n),0):
        n = n-hcf(t,n)
        t += (a-b)*(-1)**(s+1)
        s += 1
    if s%2 == 0:
        print('0')
    else:
        print('1')