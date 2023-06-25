def program4491():
    s = input()
    l = len(s)
    c = 0
    if(l==1):
        print("YES")
        exit(0)
    for i in range(l//2):
        if(s[i]!=s[-1*(i+1)]):
            c+=1
    if(c==0 and l%2!=0):
            c+=1
    if(c==1):
        print("YES")
    else:
        print("NO")