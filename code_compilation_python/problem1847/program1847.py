def program1847():
    n=input()
    lst=[]
    from itertools import permutations
    for i in range(1,len(n)):
        c=permutations(n,i)
        for j in c:
            if(j==j[::-1]):
                lst.append(j)
    lst.sort()
    s=''
    for i in lst[-1]:
        s=s+i
    print(s)
        