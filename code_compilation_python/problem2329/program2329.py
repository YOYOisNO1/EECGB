def program2329():
    n=int(input())
    t1=[]
    t2=[]
    t1=list(map(int,input().split()))
    t2=list(map(int,input().split()))
    nb=0
    for i in range(n) :
        for k in range(n) :
            if (t1[i]^t2[k] in t1) or(t1[i]^t2[k]) in t2)  :
                nb+=1
    if nb%2==0 :
        print("Karen")
    else :
        print("Koyomi")
        