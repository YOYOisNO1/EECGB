def program4494():
    s=list(input())
    count=0
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-1-i]:
            s[len(s)-1-i]=s[i]
            count+=1
        if count==1:
            break
    p="".join(s)
    if count==0:
        if len(s)%2!=0:
            if p==p[::-1]:
                print("YES")
        else:
            print("NO")
    else:
        if p==p[::-1]:
            print("YES")
        else:
            print("NO")