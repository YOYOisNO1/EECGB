    l = []
    import math
    k = 0
    
def primo(a):
        global k
        for i in range(1,int(math.sqrt(a))+1):
            if a%i == 0:
                k+=1
        if k > 1: return '1'
        else: return '2'
        
    x,y = map(int,input().split())
    p = primo(x)
    
    if y == 1:
        print(x)
    
    elif (p == '2'):
        print(-1)
    
    else:
       
        i = 2
    def div(a,b):
            global y
            global i
            
            if (a <= 1): return
            while True:
                if (a % i == 0):
                    l.append(i)
                    if (b==y):
                        if a/i != 1:
                            l.append(int(a/i))
                    break
                i+=1
        
            if (b == y): return
        
    
            div(a/i,b+1)
        div(x,2)
        if len(l) < y:
            print((-1))
        else:
            res = ''
            for i in range(y-1):
                res += str(l[i])
                res+= ' '
            res += str(l[y-1])
            print((res))
    # 1512076802006