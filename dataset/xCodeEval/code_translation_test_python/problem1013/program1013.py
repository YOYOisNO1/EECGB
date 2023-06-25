def program1013():
    l=lambda:map(int,input().split())
    a,b,c,d,e,f=l()
    print((a+b+c)**2-a*a-c*c-e*e)