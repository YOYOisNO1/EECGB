def program3309():
    a=input()
    total=0
    for i in range (1,500):
        total+=i
        if total == a :
            print("YES")
            exit()
    print("NO")