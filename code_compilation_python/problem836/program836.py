def program836():
    a,b=map(int,input().split())
    if a>b:print((a//b)+(b%(a%b))*(a%b)+(b//(a%b)))
    else:print((b//a)+((b%a)*a))