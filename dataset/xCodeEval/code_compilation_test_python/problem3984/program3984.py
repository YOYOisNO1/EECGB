def program3984():
    x=input()
    if x==3:
        print 5
    else if x==2:
        print 3
    else:
        for i in range(12345):
            if i&1 and (i>>1)*i+(i+1)/2>=x or i%2==0 and (i>>1)*i>=x:
                print i
                break