def program572():
    s = input()
    arr = s.split(" ")
    
    r = int(arr[0])
    g = int(arr[1])
    b = int(arr[2])
    
    ans = r//3 + g//3 + b//3
    
    if r > 0 and g > 0 and b > 0:
        temp = (r-1)//3 + (g-1)//3 + (b-1)//3 + 1
        ans = max(ans,temp)
    
    if r > 1 and g > 1 and b > 1:
        temp = (r-2)//3 + (g-2)//3 + (b-2)//3 + 2
        ans = max(ans,temp)
    
    
    print(ans)
    
     