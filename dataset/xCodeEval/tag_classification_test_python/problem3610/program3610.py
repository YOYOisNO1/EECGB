def program3610():
    x=map(int,input().split())
    a=x[1]
    str1=input()
    str2=''
    for i in range(a):
        if i<>0:
            str1=str(str2)
        str2=''
        j=0
        while j<len(str1):
            if str1[j]=='B' and j<>len(str1)-1 and str1[j+1]<>'B':
                str2+=str1[j+1]
                str2+=str1[j]
                j+=1
            else:
                str2+=str1[j]
            j+=1
    print(str2)