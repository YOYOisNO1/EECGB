def program1508():
    
    p = input()[-5:].replace('>', '1000').replace('<', '1001').replace('+', '1010').replace('-', '1011').replace('.', '1100').replace(',', '1101').replace('[', '1110').replace('<', '1111')[:20]
    
    n = int(p, 2)%1000003
    
    print n
    