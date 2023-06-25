def program4371():
    s=input()
    last='a'
    ans=0
    for letter in s:
        x=ord(last)-97
        y=ord(letter)-97
        ans+=min(abs(x-y),26-abs(x-y))
        last=letter
    print(ans)