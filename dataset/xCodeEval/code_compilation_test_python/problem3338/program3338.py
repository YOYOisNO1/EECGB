def program3338():
    n = int(input())
    if n%2 !=0:
        print("NO")
    else:
        tiquete=input()
        cuatros = tiquete.count("4")
        sietes = tiquete.count("7")
        if cuatros+sietes==n:
            mitad1 = tiquete[:int(len(tiquete)/2)]
            mitad2 = tiquete[int(len(tiquete)/2):(len(tiquete))]
            print(mitad1,mitad2)
            cuatros1 = mitad1.count("4")
            sietes1 = mitad1.count("7")
            cuatros2 = mitad2.count("4")
            sietes2= mitad2.count("7")
            if cuatros1==cuatros2 and 
             sietes1==sietes2:
                print("SI")
            else:
                print("NO")