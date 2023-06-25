def program1230():
    input()
    s=input()
    s+=[s-1]
    i=1
    while i<len(s):
        if s[i]!=s[i-1]:
            print('D',end='')
            i+=2
        else:   
            print(s[i],end='')
            i+=1