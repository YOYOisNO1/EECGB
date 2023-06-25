def program142():
    a,b,c = input(),input(),input()
    ans=max(a*(b+c),a+b+c,(a+b)*c,a*b*c)
    print(ans)