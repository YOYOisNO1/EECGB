def program5457():
    #----Kuzlyaev-Nikita-Codeforces-----
    #------------03.04.2020-------------
    
    alph="abcdefghijklmnopqrstuvwxyz"
    
    #-----------------------------------
    
    n=int(input())
    x,y=map(int,input().split())
    ws=x+y-2;wb=2*n-x-y
    if ws<=wb:print("White")
    else:
        print("Black")