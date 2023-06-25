def program3767():
    # coding=utf-8
    # Идея решения взята отсюда[https://rep.bntu.by/bitstream/handle/data/47746/Metod_predvaritelnyh_vychislenij_dlya_resheniya_zadach_po_informatike.pdf?sequence=1 <- google:‘"количество 2-3-чисел на отрезке"’]
    
    limit = 2000*1000*1000
    
    powers_of_2 = []
    i = 0
    while True:
        p = 2 ** i
        if p > limit:
            break
        powers_of_2.append(p)
        i += 1
    
    powers_of_3 = []
    i = 0
    while True:
        p = 3 ** i
        if p > limit:
            break
        powers_of_3.append(p)
        i += 1
    
    (l, r) = map(int, input().split())
    
    n = 0
    for i in powers_of_2:
        for j in powers_of_3:
            if l <= i * j <= r:
                n += 1
    print(n)