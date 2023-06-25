def program4063():
    n = int(input())
    A=[0]*101
    for i in range (n):
        a = int(input())
        for i in range (101):
            if i == a:
                A[i] += 1
    B=[]
    count = 0
    index1 = index2 = 0
    for i in range(101):
        if A[i] >0:
            B.append(A[i])
            index2 = index1
            index1 = i        
            count += 1
    if count == 2 and B[0] == B[1]:
        print(('YES\n',index1,index2))
    else:
        print(('NO'))   