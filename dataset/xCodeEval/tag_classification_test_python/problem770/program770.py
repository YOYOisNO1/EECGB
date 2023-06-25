def program770():
    #Amir_Python#
    t=int(input())
    answers=[]
    while t!=0:
        t=t-1
        x=int(input())
        k=list(map(int, input().split()))
        if k[x-1]==0:
            answers.append("NO")
        else:
            if k[k[x-1]-1]==0:
                answers.append("NO")
            else:
                answers.append("YES")
    for y in answers:
        print(y)