def program2515():
    #If a certain someone is looking at my code
    #You know who you are
    #Message for you
    #C++>Java
    #Python>Java
    #All Language but Java>Java
    
    x=input("").split(' ')
    a=int(x[0])
    xe=a
    b=int(x[1])
    mod=1000000007
    aa=(a*(a+1))/2
    aa*=b
    aa+=xe
    b=(b*(b-1))/2
    print((aa*b)%mod)