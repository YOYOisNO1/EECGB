def program1043():
    chess=[]*8;
    for i in range(8):a=input();chess.append(a)
    R=chess.count("WBWBWBWB");D=chess.count("BWBWBWBW");counter=R+D
    if(counter is 8):print("YES")
    else:print("NO")