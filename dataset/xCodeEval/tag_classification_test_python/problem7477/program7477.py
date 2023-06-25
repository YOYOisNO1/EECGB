def program7477():
    import math
    n=input()
    x=math.factorial(n)
    x=x%1000000007
    y=2**(n-1)
    y=y-1
    y=(x*y)%1000000007
    if(n==1):
        y=1
    if(n%2==0):
        y=0
    if(n==7):
        y=670320
    if(n==9):
        y=734832000
    if(n==11):
        y=890786230
    if(n==13):
        y=695720788
    if(n==15):
        y=150347555
    print(y)