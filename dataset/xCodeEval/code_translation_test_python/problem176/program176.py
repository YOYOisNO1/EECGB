def program176():
    n = int(input())
    
    max = 2*(n/7) + min(n%7, 2)
    min = 2*(n/7)
    if n%7 == 6:
    	min+=1
    
    print(min,) max