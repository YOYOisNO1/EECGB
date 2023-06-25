def program3007():
    pol = input('')
    pol = int(pol)
    
    tekPol = 0
    kol = 1
    
    while pol != tekPol:
        if (tekPol + kol) <= pol:
            tekPol = tekPol + kol
        else:
            tekPol = tekPol - kol
    
        kol = kol + 1
    
    kol = kol - 1
    
    print kol