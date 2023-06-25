def conv(s):
        if s == "scissors":
            return 0
        elif s == "paper":
            return 1
        else:
            return 2
    f = conv(input())
    m = conv(input())
    s = conv(input())
    if (f*m*s==0 and f+m+s==2) or (f*m*s==4 and f+m+s==5):
        if f==m:
            print("S")
        elif f==s:
            print("M")
        else:
            print("F")
    else:
        print("?")