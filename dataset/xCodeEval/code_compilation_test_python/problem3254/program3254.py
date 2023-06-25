def program3254():
    input ()
    x={"U" : 0 ; "D" :0 ; "R" :0; "L" :0;}
    for i in input()
    x[i]=x[i]+1
    print(min(x["U"]+x["D"])*2+min(x["R"]+x["L"])*2)