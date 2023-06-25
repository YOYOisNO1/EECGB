def A():
        s=input().split()
        a, b=int(s[0]), int(s[1])
        cant=a*b
        paso=1
        while cant>0:
            cant-=(a+b+1-2*paso)
            paso+=1
        if paso%2==1: print("Malvika")
        else: print("Akshat")
    A()