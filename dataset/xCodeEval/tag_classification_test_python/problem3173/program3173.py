def program3173():
    n=int(input())
    i=1
    while(True):
        n+=1
        s=str(n)
        if '8' in s:
            print(i)
            exit()
        i+=1