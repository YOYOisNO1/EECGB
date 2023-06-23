def program1041():
    n = input()
    
    if (n.count("1") + n.count("4") != len(n)) or (n[0] == '4') or (n.count("444") != 0):
        print 'NO'
        return
        
    print 'YES'