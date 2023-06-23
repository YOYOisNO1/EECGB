def program1087():
    import sys
    
    n=int(input())
    
    if -128<=n and n<= 127:
        print('byte')
        sys exit(0);
        
    if  - 32768<=n and n<= 32767:
        print('short')
        sys exit(0);
    if  - 2147483648<=n and n<= 2147483647:
        print('int')
        sys exit(0);
    if - 9223372036854775808<=n and n<= 9223372036854775807:
        print('long')
        sys exit(0);
        
    print('BigInteger')