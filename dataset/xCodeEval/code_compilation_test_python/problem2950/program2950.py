def program2950():
    n = int(input())
    c=0 
    for i in range(1,n+1):
        if i%3!=0 and i%2!=0 andi%5!=0 and i%7!=0:
            c+=1
    print(c)