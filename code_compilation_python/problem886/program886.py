def program886():
    # -*- coding: utf-8 -*-
    import sys
    
    if __name__ == '__main__':
    
        num = map(int,sys.stdin.readline().split())
        lit = []
        n = num[0]
        flag = True
    
        while flag:
            flag2 = 1
    
            for v in range(2,int(n **(0.5))+2):
    
                if n != 2 and n/v * v == n:
                    lit.append(v)
                    n /= v
                    flag2 = 0
    
                    break
                else:
                    pass
    
            if flag2 == 1:
                flag = False
    
    
        if len(lit) == 0:
            print 1
            print 0
        elif len(lit) == 1:
            print 2
        else:
            print 1
            print lit[0] * lit[1]
    