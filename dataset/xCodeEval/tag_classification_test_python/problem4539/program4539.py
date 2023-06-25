def program4539():
    x = int(input())
    hh, mm = map(int, input().split())
    
    
    if '7' in (str(hh) + str(mm)):
        ans = 0
    else:
        mins = 0
        while '7' not in (str(hh) + str(mm)) or mins % x != 0:
            mins += 1
            if mm == 0:
                if hh != 0:
                    hh -= 1
                    mm = 59
                else:
                    hh = 23
                    mm = 59
            else:
                mm -= 1
        ans = mins//x
            #print(hh, mm)
    
    
    print(ans)