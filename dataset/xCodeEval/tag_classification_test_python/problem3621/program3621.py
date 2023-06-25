def program3621():
    bla=input().split()
    l=int(bla[0])
    time=int(bla[1])
    line=input()
    f=line
    for p in range(time):
        newline=["G"]*l
        for i in range(l-1):
            if line[i]=="B" and line[i+1]=="G":
                newline[i+1]="B"
            if line[i]=="B" and line[i+1]=="B":
                newline[i]="B"
            if line[l-1]=="B":
                newline[l-1]="B"
        line=newline
    if f=="B":
        print("B")
    elif f=="G":
        print("G")
    else:
        print("").join(line)