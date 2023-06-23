def program304():
    a = input()[2:]
    b = input()[2:]
    c = input()[2:]
    d = input()[2:]
    
    if   (len(b) <= len(a)/2 and len(b) <= len(c)/2 and len(b) <= len(d)/2) or \
         (len(b) >= len(a)*2 and len(b) >= len(c)*2 and len(b) >= len(d)*2):
        print('B')
    elif (len(a) <= len(b)/2 and len(a) <= len(c)/2 and len(a) <= len(d)/2) or \
         (len(a) >= len(b)*2 and len(a) >= len(c)*2 and len(a) >= len(d)*2):
        print('A')
    elif (len(d) <= len(b)/2 and len(d) <= len(c)/2 and len(d) <= len(a)/2) or \
         (len(d) >= len(b)*2 and len(d) >= len(c)*2 and len(d) >= len(a)*2):
        print('D')
    else:
        print('C')