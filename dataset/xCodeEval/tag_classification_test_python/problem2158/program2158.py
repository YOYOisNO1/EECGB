def program2158():
    a=str(input())
    counter=0
    for x in range(len(a)):
        if int(a[x])==7 or int(a[x])==4:
            counter+=1
    if counter==len(a):
        print('YES')
    else:
        a=int(a)
        if int(a)%7==0 or int(a)%4==0 or a%47==0 or a%74==0 or a%744==0 or a%774==0 or a%777==0 or a%477==0 or a%474==0 or a%447==0 or a%444==0:
            print('YES')
        else:
            print('NO')