def program1010():
    a=input()
    b="1"
    for i in range(len(a[1:])):
        b+="0"
        
    print(int(b)-int(a[1:]))