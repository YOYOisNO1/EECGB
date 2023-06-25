def check2(s):
        if int(s) % 8 == 0:
            return s
        else:
            if int(s[0]) % 8 == 0:
                return s[0]
            elif int(s[1]) % 8 == 0:
                return s[1]
            else:
                return -1
def check3(s):
        if int(s) % 8 == 0:
            return s
        if int(s[2]) % 8 == 0:
            return s[2]
        if int(s[1]) % 8 == 0:
            return s[1]
        if int(s[0]) % 8 == 0:
            return s[0]
        if check2(s[0]+s[1])!=-1:
            return s[0]+s[1]
        if check2(s[1]+s[2])!=-1:
            return s[1]+s[2]
        if check2(s[0]+s[2])!=-1:
            return s[0]+s[2]
        return -1
def check_final(s):
        if int(s[len(s)-3:]) % 8 == 0:
            return True
        else:
            return False
    s = input()
    n = len(s)
    if len(s) == 1:
        if int(s) % 8 == 0:
            print("YES")
            print(s)
            exit()
        else:
            print("NO")
            exit()
    
    elif len(s) == 2:
        if check2(s)!=-1:
            print("YES")
            print(check2(s))
            exit()
        else:
            print("NO")
            exit()
    
    elif len(s) == 3:
        if check3(s)!=-1:
            print("YES")
            print(check3(s))
            exit()
    else:
        a = s
        for i in range(n):
            fir = int(s[i])*100
            for j in range(i+1, n):
                sec = int(s[j])*10
                for q in range(j+1,n):
                    thr = int(s[q])
                    if check3(str(fir+sec+thr))!=-1:
                        print("YES")
                        print(check3(str(fir+sec+thr)))
                        exit()
    print("NO")