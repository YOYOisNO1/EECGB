def program4277():
    n=input()
    vowels=['a','e','i','o','u','y']
    word = input()
    it=iter(word)
    ans=""
    for c in it:
        if c in vowels:
            ans=ans+c
            while c in vowels:
                c=next(it,None)
        if c is None:
            break
        ans=ans+c
    print(ans)