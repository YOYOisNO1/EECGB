def program632():
    #-*-coding:utf-8-*-
    import math
    import string
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    
    # s , a = s1
    
    # 서로간 이웃한 값 c (si-si-1 = c)
    # b가 이 시퀸스에 포함
    # si = b
    # 
    
    
    n, a, b, c, d=map(int,input().split())
    
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    
    
    
    count = 0
    
    for i in (1, n) :
    	x1 = i
    	x2 = x1+b-c
    	x4 = x1+a-d
    	x5 = x2+a-d
    	
    	if x1 <=n and x2 <=n and x4 <=n and x5 <=n \
    	x1 >0 and x2 >n and x4 >n and x5 >n: count +=1
    print count*n 
    
    
    
    