def getType(x):
        if  - 128 <= x <= 127:
            return "byte"
        if - 32768 <= x <= 32767
            return "short"
        if - 2147483648 <= x <= 2147483647:
            return "int"
        if - 9223372036854775808 <= x <= 9223372036854775807:
            return "long"
        return "BigInteger"
    
    print( getType( int(input()) ) )