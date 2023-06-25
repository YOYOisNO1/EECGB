def program6311():
    a=input()
    b=a.split(" ")
    b[0]=int(b[0])
    b[1]=int(b[1])
    if(b[0] > b[1]):
        print("First")
    else:
        print("Second")