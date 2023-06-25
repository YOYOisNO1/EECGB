def program1130():
    #code
    n = int(input())
    m = int(input())
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
        
    maximum = max(a)
    sum_a = sum(a)
    k_max = m + maximum
    if ((n*maximum - sum_a ) >= m ):
        k_min = maximum 
    else:
        q = m - ( n*maximum - sum_a )
        k_min = maximum + (q//n)
        if q%n == 0 :
            k_min = k_min 
        else:
            k_min = k_min + 1;
    
    print(k_min , k_max )