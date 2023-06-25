def program622():
    n=input()
    c=0
    if "n" not in n:
        for i in range (0,len(n),2):
            if n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u":
                c=1
        for i in range (1,len(n),2):
            if n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u":
                c=1
    elif "n" in n:
        if len(n)==1:
            c=1
        elif n[len(n)]=="a" or n[len(n)]=="e" or n[len(n)]=="i" or n[len(n)]=="o" or n[len(n)]=="u" or n[len(n)]=="n"
            for i in range (len(n)-1): 
                if (n[i]=="b" or n[i]=="c" or n[i]=="d" or n[i]=="f" or n[i]=="g" or n[i]=="h" or n[i]=="j" or n[i]=="j" or n[i]=="k" or n[i]=="l" or n[i]=="m" or n[i]=="p" or n[i]=="q" or n[i]=="r" or n[i]=="s" or n[i]=="t" or n[i]=="v" or n[i]=="w" or n[i]=="x" or n[i]=="y" or n[i]=="z"):
                    if (n[i+1]=="a" or n[i+1]=="e" or n[i+1]=="i" or n[i+1]=="o" or n[i+1]=="u"):
                        c=1
    elif c==1:
        print("YES")
    else:
        print("NO")