def program1595():
    try:
        n=int(input())
        ans=""
        if n>0:
            print(n)
        else:
            s=str(n)
            b=max(s[-1],s[-2])
            if b==s[-1]:
                ans+=s[:-1]
                break
            if b==s[-2]:
                ans+=s[:-2]+s[-1]
                break
            if ans=='-0":
                print(0)
            else:
                print(ans)
    except:
        pass