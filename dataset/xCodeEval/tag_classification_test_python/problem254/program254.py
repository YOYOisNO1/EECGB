def program254():
    import sys
    
    line = sys.stdin.readline().strip().lower();
    for i in reversed(range(0, len(line) - 1)):
        c = line[i];
        if (c != ' ') :
            last = c;
            break;
    
    if (last in ['a', 'e', 'i', 'o', 'u', 'y']):
        print("YES")
    else :
        print("NO")