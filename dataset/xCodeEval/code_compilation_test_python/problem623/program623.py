def program623():
    n=input()
    c=0
    if (n[len(n)-1]="a" or n[len(n)-1]="e" or n[len(n)-1]="i" or n[len(n)-1]="o" or n[len(n)-1]="u" or n[len(n)-1="n"]):
        for i in range (1,len(n),2):
            if (n[i]="a" or n[i]="e" or n[i]="o" or n[i]="o" or n[i]="u"):
                c=1
        for j in range (0,len(n),2):
            if (n[i]="a" or n[i]="e" or n[i]="o" or n[i]="o" or n[i]="u"):
                c=1
    if c=1:
        print("YES")
    else:
        print("NO")