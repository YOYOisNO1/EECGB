def program2416():
    import re
    n = input()
    str = input();
    str = str.replace( "_", " " )
    
    l = re.findall( r"[\w']+", str )
    x = re.findall( '\((.*?)\)', str )
    y = []
    for i in x:
        z = i.split() 
        for j in z:
            y.append( j )
    x = [ item for item in l if item not in y ]
    
    ans1 = 0
    
    try:
        ans1 = max( ans1, len( max ( x, key = len ) ) )
    except:
        ans1 = 0
    ans2 = len( y )
    print(ans1,) ans2
    