def program2289():
    source, dest, elev, tstair, telev, tedoor = map(int, input().split())
    
    totalstair = abs(source - dest) * tstair
    
    totalelev = abs(source - dest) * telev + tedoor # open at dest
    if elev != source:
    	totalelev += abs(elev - source) * telev + 2*tedoor # open + close at source
    # print(totalelev, totalstair)
    print("YES" if totalelev <= totalstair else "NO")