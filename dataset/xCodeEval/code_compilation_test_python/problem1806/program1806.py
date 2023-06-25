def program1806():
    line1 = input()
    line2 = input()
    
    n = len(line1)
    
    res = 0
    ind = 0
    
    while ind < n - 1:
        count = 0
        if line1[ind] == '0':
            count += 1
    
        if line1[ind+1] == '0':
            count += 1
    
        if line2[ind] == '0':
            count += 1
    
        if line2[ind+1] == '0':
            count += 1
    
        if (count == 3):
            res += 1
            ind += 2
        elif count == 4:
            res += 1
            if ind + 2 <= n - 1:
                if line1[ind + 2] == '0' and line2[ind + 2] == '0':
                    res += 1
                    ind += 3
            else:
                ind += 2
        else:
            ind += 1
    
    print(res)