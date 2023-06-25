def program135():
    import string
    n=input()
    s=input()
    maxi=-1
    ans=[]
    for i in range(n):
        t=s[i]
        if t in string.lowercase:
            if t not in ans:
                ans.append(s[i])
        else:
            maxi=max(maxi,len(ans))
            ans=[]    
    print(max(maxi,len(ans)))