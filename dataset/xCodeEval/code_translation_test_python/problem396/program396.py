def program396():
    # -*- coding: utf-8 -*-
    """
    Created on Sat Jul 18 02:20:19 2020
    
    @author: thiva
    """
    
    Sums = [0,5]
    val = 2
    for i in range(30):
        val = val * 2
        Sums.append(5*(val - 1))
    
    n = int(input())
    
    for i in range(len(Sums)):
        if(n <= Sums[i]):
            checkpoint = i-1
            break
    
    excess = n - Sums[checkpoint]
    ans = (excess - 1)//(Sums[checkpoint]//5 + 1)
    
    People = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
    print(People[ans])