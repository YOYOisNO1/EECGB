def program153():
    n=input()
    text=input().split()
    maxd=0
    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(text)):
        cnt=0
        for j in range(len(text[i])):
            if text[i][j] in l:
                cnt+=1
            if cnt>maxd:
                maxd=cnt
    print(maxd)
                