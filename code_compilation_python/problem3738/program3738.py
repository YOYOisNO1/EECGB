def program3738():
    from math import *
    import time
    l1=input().split(" ")
    l2=input().split(" ")
    if(l1[0]==l2[0] and l1[1]==l2[1] or l1[0]==l2[0] and l1[2]==l2[2] or l1[2]==l2[2] and l1[1]==l2[1]):
    	print("YES")
    else:
    	print("NO")
    # print(time.time()-t1)