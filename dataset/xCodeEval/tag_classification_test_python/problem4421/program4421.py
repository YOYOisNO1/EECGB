def program4421():
    l=list(input())
    j=1
    e=0
    while(j<len(l)-2):
        if(l[j]=='d' and l[j+1]=='o' and l[j+2]=='t' and j<len(l)-3):
            l[j]='.'
            l[j+1]='0'
            l[j+2]='0'
            j+=3
        elif(l[j]=='a' and l[j+1]=='t' and e==0):
            l[j]='@'
            l[j+1]='0'
            j+=2
            e+=1
        else:
            j+=1
    for i in range(len(l)):
        if(l[i]!='0'):
            print(l[i],end="")
        
            