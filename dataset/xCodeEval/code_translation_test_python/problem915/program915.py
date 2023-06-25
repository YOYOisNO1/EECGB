    # -*- coding:utf-8 -*-
    #[n, m] = [int(x) for x in input().split()]
    
def some_func():
        """
        """
    
        n,k = [int(x) for x in input().split()]
        n_list = [int(x) for x in input().split()]
        cache_dic = {}
        cost = 0
    
    
        for i in range(0,k):
            if i not in n_list:
                cost+=1
        if k in n_list:
            cost+=1
        return cost
    
    
    
    if __name__ == '__main__':
        print(some_func())
    