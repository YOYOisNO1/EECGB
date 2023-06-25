def program3445():
    n=int(input())
    s=input()
    i=0
    j=0
    while(j<n):
        i=i+1
        j=j+i
        print(s[j-1],end='')