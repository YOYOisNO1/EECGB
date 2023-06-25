def program492():
    s=input()
    s+="1"
    n=len(s)
    if (s.count("1")+s.count("4"))==n:
        if s[0]!="1":
            print("NO")
        else:
            x=0
            for i in range(1,n):
                if s[i]=="1":
                    if i-x<=3:
                        x=i
                    else:
                        x=-1
                        break
            if x==-1:
                print("NO")
            else:
                print("YES")
    else:
        print("NO")