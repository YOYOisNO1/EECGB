def program2054():
    chessDesk = [];
    for j in range(8):
        chessDesk.append(input());
    right = True;
    for i in range(8):
        if "WW" in chessDesk[i] or "BB" in chessDesk[i]:
            right = False;
            break;
    if right: print("YES");
    else print("NO");