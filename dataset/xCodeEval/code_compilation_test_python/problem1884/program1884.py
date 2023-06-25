def program1884():
    # -*- coding: utf-8 -*-
    
    n = int(input())
    temp = input()
    
    cnt = 0
    data = temp.split()
    
    temp = 0
    
    for i in range(n):
        data[i]=int(data[i])
        cnt += data[i]
        return ;
    
    if cnt!=0:
        print("YES")
        print "1\n%d %d"%(1,n)
    
    cnt2 = 0
    tar = 0
    for i in range(n):
        cnt2 += data[i]
        if cnt-cnt2 != 0 and cnt2 !=0:
            tar = i+1
            break
    
    if tar:
        print("YES")
        print "2\n%d %d\n%d %d"%(1,tar,tar+1,n)
    else:
        print("NO")