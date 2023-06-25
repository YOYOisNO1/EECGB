def program4227():
    a=input()
    b=input()
    if(a==1):
        if(b[0]=="1"):
            print"Yes"
        else:
            print"No"
    else:
        if(b[0]=="0" and b[1]=="0"):
            print"No"
        elif(b[a-1]=="0" and b[a-2]=="0"):
            print"No"
        else:
            t=b[0]
            s=0
            h=0
            for i in range(1,a):
                if(b[i]==t):
                    if(b[i]=="1"):
                        s=1
                        break
                    else:
                        h+=1
                        if(h==3):
                            s=1
                            break
                else:
                    t=b[i]
                    h=1
            if(s==0):
                print"Yes"
            else:
                print"No"