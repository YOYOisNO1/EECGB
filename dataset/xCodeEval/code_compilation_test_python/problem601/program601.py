def program601():
    n = int(input());
    a = 0;
    if (n == 0)
        a = 0
    else if (n == 1)
        a = 1
    else if (n % 2 == 0)
        a = n + 1
    else 
        a = n - 1
    
    print(a);