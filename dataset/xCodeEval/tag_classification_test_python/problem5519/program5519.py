def program5519():
    a= list(map(int,input().split()))
    import math
    b=[]
    if a[0]*a[1]+2*a[3]< a[0]*a[2]+2*a[4]:print("First")
    if a[0]*a[1]+2*a[3]> a[0]*a[2]+2*a[4]:print("Second")
    if a[0]*a[1]+2*a[3]== a[0]*a[2]+2*a[4]:print("Friendship")