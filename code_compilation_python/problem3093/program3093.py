def program3093():
    n = int(input())
    s = input()
    l =[]
    maxi = 0
    for i in range(n):
        if s[i].isupper():
            maxi = max(maxi,len(set(l)))
            l=[]
        else:
            l.append(s[i])
    maxi = max(maxi,len(set(l))
    print(maxi)