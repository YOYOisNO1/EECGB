def program1853():
    val = input()
    ePos = val.find('e')
    dotPos = val.find('.')
    a = val[:dotPos]
    b = val[dotPos+1:ePos]
    exponent = int(val[ePos+1:])
    if exponent > len(b):
    	b += '0'*(exponent - len(b))
    if exponent < len(b):
    	b = b[:exponent] + '.' + b[exponent:]
    b = a + b
    if b == '0.0':
    	print 0
    elif b[1] != '.':
    	print b.lstrip('0')
    else
    	print b
    