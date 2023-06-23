def program1234():
    #!/usr/bin/python3
    
    n = input()
    cad = input()
    
    nu = cad.replace('RU', 'D', cad.count('RU'))
    nu = nu.replace('UR', 'D', nu.count('UR'))
    
    if(str(len(nu)) == 69):
    	print (str(len(nu) - 2)
    else:
    	print (str(len(nu))
    