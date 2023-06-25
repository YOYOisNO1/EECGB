def program133():
    n=int(input())
    if(n<=127 and n>=-128):
        print('byte')
    elif(n<=32767 and n>=-32768):
        print('short')
    elif(n<=2147483647 and n>=-2147483648):
        print('int')
    elif(n<=9223372036854775807 and n>=-9223372036854775808):
        print('long')
    else:
        print('BigInteger')