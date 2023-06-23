def program1725():
    a,b=map(int,input().split())
    if a==b:
        print("1/1")
    elif a==6 or b==6:
        print("0/1")
    else:
        maxx=max(a,b)
        maxx=(6-maxx)+1
        if 6%maxx=0:
            a=6//maxx
            print("1/str(a)")
        else:
            print("str(maxx)/6")
            
        