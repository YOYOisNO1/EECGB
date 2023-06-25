def program5101():
    s = input().split("|")
    w = input()
    for c in w:
        if(len(s[0])<len(s[1])):
            s[0]+=c
        else:
            s[1]+=c
    if(len(s[0])==len(s[1])):
        print(s[0]+"|"+s[1])
    else:
        print("Impossible")