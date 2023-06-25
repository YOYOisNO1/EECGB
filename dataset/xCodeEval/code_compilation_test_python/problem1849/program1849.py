def program1849():
    from itertools import permutations
    s=input()
    d={}
    c=1
    m=-1
    l=[]
    d={}
    for i in range(len(s)):
        l.append(list(permutations(s,i+1)))
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j]=''.join(l[i][j])
    for i in l:
        for j in i:
            if(j==j[::-1]):
                if(j not in d):
                    d[j]=0
    print(max(d))