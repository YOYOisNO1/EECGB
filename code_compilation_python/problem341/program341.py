def program341():
    s = input()
    l = len(s)
    le = int(l/2)
    if(le==0):
        print(s)
    else:
        k=""
        k = str(k)
        for i in range(le):
            if(l%2==0):
                k = str(s[i]+s[l-i-1]+k)
            else:
                k += str(s[l-i-1]+s[i])
    if(l%2!=0):
        k =  s[le]+k
    print(k)
            