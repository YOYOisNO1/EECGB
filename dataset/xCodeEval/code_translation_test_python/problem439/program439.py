def program439():
    n=int(input())
    l1=[]
    l2=[]
    if n==1:
        print(1)
    else:
        for i in range(n):
            l1.append(1)
        a = 1
        while a < n:
            l2 = [1]
            for i in range(n - 1):
                l2.append(l1[i + 1] + l2[i])
            l1 = l2
            a += 1
        print(l2[-1])
    