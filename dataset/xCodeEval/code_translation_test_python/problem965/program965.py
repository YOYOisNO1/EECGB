def program965():
    n=input()
    s=list(str(input()))
    i=0
    while i<n-2:
        if s[i]=='o'and s[i+1]=='g' and s[i+2]=='o':
            s[i],s[i+1],s[i+2]="*","*","*"
            while i<n-4:
                #print(s)
                if s[i+3]=='g' and s[i+4]=='o':
                    s[i+3],s[i+4]='',''
                    i=i+2
                else:
                    break
        i=i+1
       # print(s)
    print("").join(s)
    