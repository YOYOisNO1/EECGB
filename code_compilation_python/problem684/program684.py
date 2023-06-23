def program684():
    input() 
    k = "YES" 
    a = input() 
    a = list(a) 
    for i in range(len(a)-2): 
     if a[i] == '0': 
     if a[i+2] == '1': 
     k = "NO" 
     break 
     if a[i] == '1': 
     if a[i+1] == '1': 
     k = "NO" 
     break 
    print(k)