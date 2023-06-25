def program1625():
    n=input()
    s=map(int,input().strip().split())
    a=[]
    k=0
    for i in s:
        if i!=5:
            a.append(i)
        else:
            pass
    a.sort()
    for i in s:
        k+=i
    k=float(k)/n
    count=0
    for i in range(len(a)):
            if k<4.5:
                while a[i]<5:
                        a[i]+=1
                        k+=float(1)/n
            else:
                break
            count+=1
    print(count)