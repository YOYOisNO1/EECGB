def program841():
    up, down, unk = [int(x) for x in input().split()]
    all_unk_up = up + unk
    all_unk_down = down + unk
    if up > all_unk_down:
        print("+")
    elif down > all_unk_up:
        print("-")
    elif up == down and unk == 0:
        print("0")
    else:
        print("?")
    
    
    
    
    
    
    
    
    
    
    # if (down < up and down + unk >= up) or (up < down and up + unk >= down) or (unk >= abs(up-down) and unk > 0):
    #     print("?")
    # elif up > down + unk:
    #     print("+")
    # elif down > up + unk:
    #     print("-")
    # else:
    #     print("0")