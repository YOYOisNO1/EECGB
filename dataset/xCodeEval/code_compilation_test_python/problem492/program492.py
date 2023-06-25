def program492():
    s = input()
    if len(s)>6:
        for i in range(7,len(s)):
            if s[i] == 1 and s[0:i].count('0') == 6:
                print("yes")
                break
        else:
            print("no")
    else:
        print("no"