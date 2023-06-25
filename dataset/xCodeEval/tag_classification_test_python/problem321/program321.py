def program321():
    n , a = int(input()) , input()
    d = 0
    for i in range(n-2):
        if a[i]==a[i+1]==a[i+2]=='x':
            d+=1
    print(d)