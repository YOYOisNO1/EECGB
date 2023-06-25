def program58():
    h = int(input())
    m = int(input())
    s = int(input())
    t1 = int(input())
    t2 = int(input()) 
    
    if t2>t1:
        if h not in list(range(t1,t2+1)) and int(m/5) not in list(range(t1,t2+1)) and int(s/5) not in list(range(t1,t2+1)):
            print ("YES")
        elif h not in list(range(t2,t1+12)) and int(m/5) not in list(range(t2,t1+12))and int(s/5) not in list(range(t2,t1+12)):
            print ("YES")
        else: 
            print ("NO")
            
    else:
        if h not in list(range(t1,t2+12)) and int(m/5) not in list(range(t1,t2+12)) and int(s/5) not in list(range(t1,t2+12)):
            print ("YES")
        elif h not in list(range(t2,t1)) and int(m/5) not in list(range(t2,t1))and int(s/5) not in list(range(t2,t1)):
            print ("YES")
        else:
            print("NO")