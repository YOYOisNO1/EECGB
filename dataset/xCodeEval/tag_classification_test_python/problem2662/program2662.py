def program2662():
    x=str(input())
    y=int(0)
    import sys
    if len(x)<=2:
        print("No")
        sys.exit()
    else:
        for i in range(len(x)-2):
            if x[i]=='A' and x[i+1]=='B'and x[i+2] =='C':
                print("Yes")
                break
            elif x[i]=='C' and x[i+1]=='B'and x[i+2] =='A':
                print("Yes")
                break
            elif x[i]=='B' and x[i+1]=='A'and x[i+2] =='C':
                print("Yes")
                break
            elif x[i]=='C' and x[i+1]=='A'and x[i+2] =='B':
                print("Yes")
                break
            elif x[i]=='B' and x[i+1]=='C'and x[i+2] =='A':
                print("Yes")
                break
            elif x[i]=='A' and x[i+1]=='C'and x[i+2] =='B':
                print("Yes")
                break
            else:
                y+=1
    if y==len(x)-2:
        print("No")
    