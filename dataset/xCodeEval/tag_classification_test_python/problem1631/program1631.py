def program1631():
    t1 = t2 = t3 = False;
    s = input();
    for sym in s:
        if 'a' <= sym <= 'z':
            t1 = True;
        if 'A' <= sym <= 'Z':
            t2 = True;
        if sym.isdigit():
            t3 = True;
    if t1 and t2 and t3 and len(s) >= 5:
        print('Correct');
    else:
        print('Too weak');