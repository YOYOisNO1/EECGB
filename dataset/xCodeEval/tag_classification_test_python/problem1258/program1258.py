    # -*- coding:utf-8 -*-
    
    import sys
def some_func():
        """
        """
        n = int(input())
    
        flag1=0
        flag2=0
        flag3=0
        for i in range(n):
            n1,n2 = [int(x) for x in input().split()]
            if n1%2:
                if n2%2:
                    flag1+=1
                else:
                    flag2+=1
            else:
                if n2%2:
                    flag3+=1
    
        if not (flag1+flag2)%2 and  not(flag1+flag3)%2:
            print(0)
        elif (flag1+flag2)%2 and (flag1+flag3)%2 and flag2+flag3 :
            print(1)
        else:
            print(-1)
    
    
    
    
    if __name__ == '__main__':
        some_func()