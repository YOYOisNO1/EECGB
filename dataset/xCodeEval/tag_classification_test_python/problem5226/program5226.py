def program5226():
    #code
    k = input()
    f,s = map(str,input().split())
    x = ['6','7','8','9','T','J','Q','K','A']
    if f[1]!=s[1]:
        if f[1]==k:
            print("YES")
        else:
            print("NO")
    else:
        if x.index(f[0])>x.index(s[0]):
            print("YES")
        else:
            print("NO")