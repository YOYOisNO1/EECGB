def program1516():
    n = input()
    s = input().strip()
    
    if n == 1:
        print("Yes")
        exit()
    
    x = [0] * 26
    for c in s:
        x[ord(c) - ord('a')] += 1
    
    for l in x:
        if l > 1:
            print("Yes")
            exit()
    
    print("No")