def program2524():
    a,b,c,d=list(map(int,input().split()))
    if(a==b and b==c and c==d):
        print("3")
    elif(((a==b) and (b==c)) or ((a==b) and  (b==d)) or ((a==c)and(c==d))or ((b==c)and(c==d))):
        print("2")
    elif (((a==b) and (c==d)) or (( a==c)and( b==d))or ((a==d)and(b==c))):
        print("2")
    elif( ( a==b) or (a==c) or( a==d)or(b==c) or(b==d)or(c==d)) :
        print("1")
    else:
        print("0")