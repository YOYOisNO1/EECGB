def program4394():
    s=input()
    print(s[0]+s[1:len(s)-1].replace("at","@",1).replace("dot",".") + s[len(s)-1])