def program1590():
    a,b=map(int,input().split())
    i=1
    while True:
        if i%2!=0:
            a-=i
            if a<0:
                print("Vladik")
                break
        else:
            b-=i
            if b<0:
                print("Valera")
                break
        i+=1
    