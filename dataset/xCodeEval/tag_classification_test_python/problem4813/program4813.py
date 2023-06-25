def program4813():
    n = int(input())
    k = input()
    q = [0,0,0,0]
    for i in k:
        if i =='U':
            q[0]+=1
        if i =='D':
            q[1]+=1
        if i =='L':
            q[2]+=1
        if i =='R':
            q[3]+=1
    print(min(q[0],q[1])*2+min(q[2],q[3])*2)