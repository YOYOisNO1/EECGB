def program3224():
    a,b=map(int,input().split());c=[list(input().split()) for _ in " "*b];z=['a'];t=[]
    for i in range(1,a):
        for j in z:
            for k in c:
                if j[0]==k[1]:t.append(k[0]+j[1::])
        z=t;t=[]
    print(len(z))