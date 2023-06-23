def factors(x):
       l=[]
       for i in range(1, x + 1):
           if x % i == 0:
               l.append(i)
        return l
    
def lcm(x, y):
       # choose the greater number
       if x > y:
           greater = x
       else:
           greater = y
       while(True):
           if((greater % x == 0) and (greater % y == 0)):
               lcm = greater
               break
           greater += 1
       return lcm
    x=int(input())
    l=factors(x)
    m=[]
    i=len(l)-1
    while i>=1:
        if lcm(l[i],l[i-1])==x:
            m.append(l[i-1],l[i])
            i=i-1
        else:
            break
    m.sort
    print(m[0])
        