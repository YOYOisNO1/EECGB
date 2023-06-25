def program2539():
    n, m = [int(x) for x in input().split()]
    
    p = [int(x) for x in input().split()]
    
    p.sort()
    
    difference_list = [abs(p[x]-p[x+1]) for x in range(m-1)]
    
    new_l = [difference_list[x:(x+n-1)] for x in range(m-n+1)]
    
    print(min([sum(x) for x in new_l]))