def program231():
    s=input()
    ans="hello"
    j=0;i=0
    while i < len(s) and j < 5:
        if s[i]==ans[j]:
            j+=1
        i+=1
    if j==5:
        print("YES")
    else:
        print("NO")