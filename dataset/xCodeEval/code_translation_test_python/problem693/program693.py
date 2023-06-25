    # -*- coding:utf-8 -*-
    import sys
def is_ok(v,n):
        v= str(v)
        n= str(n)
        for i in v:
            if i in n:
                return 1
        return 0
    
    
def some_func():
        """
        """
        n = input()
        cache_dic = {}
        for v in range(1,int(n**0.5)+2):
            if n%v==0:
                cache_dic[v]=1
                cache_dic[n/v]=1
    
        count = 0
        
        for v in cache_dic.keys():
            if is_ok(v,n):
                count+=1
        print(count)
    
    
    
    if __name__ == '__main__':
        some_func()
    
    
    