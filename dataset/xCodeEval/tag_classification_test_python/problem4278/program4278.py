def program4278():
    n=int(input())
    l=list(input())
    p=['a','e','i','o','u','y']
    i=0
    l.append(" ")
    while l[i]!=" ":
        if l[i].lower() in p and l[i+1].lower() in p:
            del l[i+1]
        else:
            i+=1
    print("".join(l))