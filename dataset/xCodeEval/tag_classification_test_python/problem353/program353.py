def program353():
    t = input()
    k = t[0]+t[2]+t[4]+t[3]+t[1]
    l = int(k)
    ans = l**5
    i=0
    st=""
    while(i<5):
        st = st + str(ans%10)
        ans /=10
        i+=1
    print(st[::-1])   
    