def program633():
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
    
    
    a, b, c=map(int,input().split())
    
    if a == b and c == 0 : print("YES")
    elif c!=0 :
    	if (b - a) % c == 0 :  print("YES")
    	else : print("NO")
    else : print "NO