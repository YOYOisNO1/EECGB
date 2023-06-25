def program2860():
    total = int(input());
    exes = input().split(" ");
    
    biceps = 0;
    back = 0;
    chest = 0;
    
    for i in range(int(total/3 + 1)):
        print "-----";
        if i*3 < total: chest += int(exes[i*3]);
        if (i*3)+1 < total: biceps += int(exes[(i*3)+1]);
        if (i*3)+2 < total: back += int(exes[(i*3)+2]);
    
    if chest > biceps and chest > back: print "chest";
    else if biceps > chest and biceps > back: print "biceps";
    else: print "chest";