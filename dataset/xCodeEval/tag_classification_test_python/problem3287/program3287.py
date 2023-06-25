def program3287():
    n = input()
    my_list = []
    i=1
    while (i<=n):
        if (n%i==0):
            my_list.append((i,n/i))
        i+=1
    
    
    for t in my_list:
        if t[0] - t[1] >= 0 and t[0] - t[1] <min:
            min = t[0]-t[1]
            c,d = t
    print(d,c)
    
                
            
        