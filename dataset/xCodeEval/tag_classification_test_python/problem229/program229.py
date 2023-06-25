def program229():
    s=input()
    a='hello'
    i=j=0
    while j<len(s) and i<5:
        if s[j]==a[i]:
            i+=1
        j+=1
    print("YES") if i==5 else "NO"