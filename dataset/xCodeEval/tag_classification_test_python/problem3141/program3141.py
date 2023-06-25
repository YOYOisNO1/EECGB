def program3141():
    n=input("")
    if int(n[len(n)-1])<5:
        print(int(n)-int(n[len(n)-1]))
    elif int(n[len(n)-1])>5:
        print(int(n)-int(n[len(n)-1])+10)
    else:
        print(int(n)-int(n[len(n)-1]))