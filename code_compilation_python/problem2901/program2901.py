def program2901():
    //Number of cubes
    n = int(input())
    //cube number use at current level
    lv_n = 0
    //the maximum height of the pyramid
    hmax = 0
    
    while n>0:
       hmax += 1
       lv_n += hmax
       n -= lv_n
    
    print (hmax)