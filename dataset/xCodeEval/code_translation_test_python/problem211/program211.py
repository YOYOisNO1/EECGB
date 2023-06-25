def program211():
    s=str(input())
    x=""
    for i in range(len(s)):
        if s[i]=="h" or s[i]=="e" or s[i]=="l" or s[i]=="o":
            x=x+s[i]
    s=x.lower()
    for i in range(len(s)):
        if(s.find("hh")!=-1):
            s=s.replace("hh", "h")
        if(s.find("ee")!=-1):
            s=s.replace("ee", "e")
        if (s.find("lll")!=-1):
            s=s.replace("lll", "ll")
        if (s.find("oo")!=-1):
            s=s.replace("oo", "o")
    if (s.find("h")!=-1):
        s=s.replace(s[0:s.index("h")+1],"1",1)
    if(s.find("1")!=-1) and (s.find("e")!=-1):
        if (s.find("1e")==-1):
            s=s.replace(s[int(s.index("1")+1):s.index("e")+1],"2",1)
        else:
            s = s.replace("e", "2", 1)
    if(s.find("12")!=-1) and (s.find("l")!=-1):
        if (s.find("12l") == -1):
            s=s.replace(s[int(s.index("2")+1):s.index("l")+1],"3",1)
        else:
            s = s.replace("l", "3", 1)
    if(s.find("123")!=-1) and (s.find("l")!=-1):
        if (s.find("123l") == -1):
            s=s.replace(s[int(s.index("3")+1):s.index("l")+1],"4",1)
        else:
            s = s.replace("l", "4", 1)
    if(s.find("1234")!=-1) and (s.find("o")!=-1):
        if (s.find("1234o") == -1):
            s=s.replace(s[int(s.index("4")+1):s.index("o")+1],"5",1)
        else:
            s = s.replace("o", "5", 1)
    # print(s)
    if(s.find("12345")!=-1):
        print("YES")
    else:
        print("NO")
    
    
    
    
    # if s.find('h(.*?)e(.*?)l(.*?)l(.*?)o')!=-1:
    #     print("NO")
    # else:print("YES")