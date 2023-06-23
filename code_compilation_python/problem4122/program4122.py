def program4122():
    a=list(map(int,input().split()))
    b=[]
    c=[]
    d=[]
    for i in range(a[0]):b.append(list(input()))
    for i in range(a[0]):
        for j in range(a[1]):
            if b[i][j]=="#":c.append("b["+str(i)+"]["+str(j)+"]")
    for i in range(a[0]-2):
        for j in range(a[1]-2):
            if b[i][j]=="#" and b[i][j+1]=="#"  and b[i][j+2]=="#" and b[i+1][j]=="#" and b[i+1][j+2]=="#" and b[i+2][j]=="#" and b[i+2][j+1]=="#" and b[i+2][j+2]=="#":
                if "b["+str(i)+"]["+str(j)+"]" not in d:d.append("b["+str(i)+"]["+str(j)+"]")
                if "b["+str(i)+"]["+str(j+1)+"]" not in d:d.append("b["+str(i)+"]["+str(j+1)+"]")
                if "b["+str(i)+"]["+str(j+2)+"]" not in d:d.append("b["+str(i)+"]["+str(j+2)+"]")
                if "b["+str(i+1)+"]["+str(j)+"]" not in d:d.append("b["+str(i+1)+"]["+str(j)+"]")
                if "b["+str(i+1)+"]["+str(j+2)+"]" not in d:d.append("b["+str(i+1)+"]["+str(j+2)+"]")
                if "b["+str(i+2)+"]["+str(j)+"]" not in d:d.append("b["+str(i+2)+"]["+str(j)+"]")
                if "b["+str(i+2)+"]["+str(j+1)+"]" not in d:d.append("b["+str(i+2)+"]["+str(j+1)+"]")
                if "b["+str(i+2)+"]["+str(j+2)+"]" not in d:d.append("b["+str(i+2)+"]["+str(j+2)+"]")
    if set(c)==set(d):print("YES")
    else:print("NO")