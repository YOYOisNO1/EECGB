    # -*- coding:utf-8 -*-
    import sys
def some_func():
        """
        """
    
        n_list= map(str, input().replace('\n','').split(' '))
    
        if "week" in n_list:
            n = int(n_list[0])
            if n==5 or n==6:
                print(53)
            else:
                print(52)
        else:
            n = int(n_list[0])
            if n<30:
                print(12)
            elif n == 30:
                print(11)
            else:
                print(7)
    
    
    
    
    
    if __name__ == '__main__':
        some_func()