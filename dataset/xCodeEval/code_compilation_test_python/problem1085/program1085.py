def program1085():
    x=int(input())
    if(x<=127&&x>=-128):
        print("byte")
    elif(x<=32767&&x>=-32768):
        print("short")
    elif(x<=2147483647&&x>=-2147483648 ):
        print("int")
    elif(x<=9223372036854775807&&x>=-9223372036854775808 ):
        print("long")
    else:
        print("BigInteger")