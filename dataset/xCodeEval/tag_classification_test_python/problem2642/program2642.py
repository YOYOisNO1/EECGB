def program2642():
    n, m = map (int, input ().split ());
    data = list (map (int, input ().split ()));
    
    a = [];
    for i in data :
        count = 0;
        b = list (a);
        while (sum (b) + i > m) :
            mmm = max (b);
            b.remove (mmm);
            count += 1;
            
        a.append (i);
        print((count,) end = " ");