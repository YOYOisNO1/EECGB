def program2726():
    s = list(input()); t = list(input())
    h1 = int(s[0]+s[1]); m1 = int(s[3]+s[4]); h2 = int(t[0]+t[1]); m2 = int(t[3]+t[4])
    ah = h1-h2
    am = m1-m2
    if am < 0:
        am += 60
        ah -= 1
    if ah < 0:
        ah += 24
    
    if am < 10:
        am = '0'+str(am)
    if ah < 10:
        ah = '0'+str(ah)
    print(str(ah)+":"+str(am))