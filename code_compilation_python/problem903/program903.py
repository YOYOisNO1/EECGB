def program903():
    sbuf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    Ans1=''
    Ans2=''
    s=input()
    f=1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            f=0
    if f == 0 :
        print "Impossible"
    else:
        bukva = ''
        for i in sbuf:
            if s.count(i) > 1:
                bukva = i
        r= -1
        l= -1
        for i in range(len(s)):
            if s[i] ==bukva and l == -1:
                l=i
            elif s[i] == bukva:
                r=i
        lenght = r-l-1
        if 1: # 13
            if lenght%2 == 0:
                for i in range(len(s)):
                    if s[i] ==bukva:
                        index = i
                        Ans2+=bukva
                        break
                    Ans1+=s[i]
                bufStr = s[l+1:r]
                for i in range(len(bufStr)/2):
                    Ans2+=bufStr[i]
    
                bufStr = bufStr[::-1]
                for i in range(len(bufStr)/2):
                    Ans1+=bufStr[i]
    
                for i in range(13-len(Ans2)):
                    Ans2=s[r+i+1]+Ans2
                s=s[::-1]
    
                for i in range(13-len(Ans1)):
                    Ans1=s[i]+Ans1
                print Ans2
                print Ans1
            elif lenght%2 == 1:
                for i in range(len(s)):
                    if s[i] == bukva:
                        index = i
                        Ans2 += bukva
                        break
                    Ans1+=s[i]
                bufStr = s[l+1:r]
    
                
                for i in range(len(bufStr)/2):
                    Ans2+=bufStr[i]
                bufStr = bufStr[::-1]
                for i in range(len(bufStr)/2):
                    Ans1+=bufStr[i]
                Ans1+=bufStr[len(bufStr)/2]
    
    
                
                for i in range(13-len(Ans2)):
                    Ans2=s[r+i+1]+Ans2
                s=s[::-1]
                for i in range(13-len(Ans1)):
                    Ans1=s[i]+Ans1
                print Ans2
                print Ans1  
                
                    
                    
                