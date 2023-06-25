    import sys;
    
    #sys.stdin = open("input.txt", "r");
    #sys.stdout = open("output.txt", "w");
    
def ria():
        return [int(x) for x in input().split()];
    
    n, m = (int(x) for x in input().split());
    
    a = ria();
    b = ria();
    a.sort();
    b.sort();
    
    tf = 0;
    
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                tf = 1;
                atg = a[i];
                break;
        if ( tf == 1 ):
            break;
    
    if ( tf == 1 ):
        ans = atg;
    else:
        ans = str(min(a[0], b[0]) + str(max(a[0], b[0])));
    
    
    print(ans);
    
    
    #sys.stdout.close();