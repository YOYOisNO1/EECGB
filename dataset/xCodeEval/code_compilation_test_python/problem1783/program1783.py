def program1783():
    walruses,chips=map(int,input().split())
    while True:
        for i in range (walruses):
            if chips>i+1:
                chips=chips-(i+1)
            else:
                break
    print (chips)