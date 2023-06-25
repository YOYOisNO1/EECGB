def program4446():
    a=input()
    print(a[0]+a[1:len(a)-1].replace("at", "@",1).replace("dot",".")+a[len(a)-1])