def fu( st = str ):
        tf = 1;
        n = len(st);
        for i in range(0,n,1):
            if st[i] != st[n-1-i]:
                tf = 0;
        if tf == 0:
            return 0;
        else:
            return 1;
        
    st = input();
    tf = 0;
    if st[-1] == "\n":
        st = st[0:-1];
    n = len(st);
    for i in range(0,n,1):
        if st[n-1-i] != st[i]:
            st1 = st[0:i] + st[n-1-i] +  st[i+1:n];
        else:
            st1 = st[0:i] + "." + st[i+1:n];
        if fu(st1) == 1:
            tf = 1;
            break;
    
    if tf == 0:
        print("NO");
    else:
        print("YES");