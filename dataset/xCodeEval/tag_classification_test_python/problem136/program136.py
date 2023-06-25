def program136():
    n=input()
    
    j=(int(n))
    
    
    
    if len(str(abs(j)))<=3 and j>=-128 and j<=127:
        print("byte")
    elif len(str(abs(j)))>=3 and len(str(abs(j)))<=5 and j>=-32768 and j<=32767:
        print("short")
    elif len(str(abs(j)))>=5 and len(str(abs(j)))<=10 and j>=-2147483648 and j<=2147483647:
        print("int")
    elif len(str(abs(j)))>=10 and len(str(abs(j)))<=19 and j>=-9223372036854775808 and j<=9223372036854775807:
        print("long")
    else:
        print("BigInteger")