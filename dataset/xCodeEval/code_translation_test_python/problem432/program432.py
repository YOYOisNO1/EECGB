def program432():
    n=int(input())
    ans=2*3*4*(4**(n-3))
    ans2=9*(n-3)*(4**(n-3))
    print(ans+ans2)