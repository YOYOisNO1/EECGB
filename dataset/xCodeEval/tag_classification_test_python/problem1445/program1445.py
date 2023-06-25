def program1445():
    a,b,c,d = list(map(int,input().split()))
    a = max(3*a /10,  a- (a/250 * c)) ; b = max (3*b /10, b- (b/250 * d))
    if(a == b): print("Tie")
    elif(a > b): print("Misha")
    else: print("Vasya")