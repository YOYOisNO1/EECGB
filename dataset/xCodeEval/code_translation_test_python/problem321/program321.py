def program321():
    s=str(input())
    l=s.split("WUB")
    for q in l:
        if(q==""):
            continue
        print(q,end=" ")