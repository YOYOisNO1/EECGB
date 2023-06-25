    from itertools import combinations
    #import numpy as np
    
def prime_divisors(n):
        a = []
        i = 2
        while i*i <= n:
            if n % i == 0:
                a.append(i)
                n //= i
            else:
                i += 1
        a.append(n)
        a.sort(reverse=True)
        return a
        
    n = int(input())
    npr = [2,3,5,7,11,13,17,19,23,29]
    
    # поиск всех списков-вариантов множителей "n"
    res =[]
    # разложение на простые делители "n"
    delit = prime_divisors(n)
    for i in range(2,len(delit)) :
        # все комбинации перебора делителей,
        # начиная с двух делителей до всех делителей
        data = list(combinations(delit, i))
        for j in data:
            jj = list(j)
            
            # здесь пытался применить prod от numpy,
            # но ниже при нахождении "ss" шло 
            # переполнение (????)
            temp = 1
            for k in jj:
                temp *= k
            temp1 = n//temp
            
            # добавление к набору делителей
            # частного от "n" к произведению делителей
            jj.append(temp1)
            jj.sort(reverse=True)
            
            # добавление набора из произведения 
            # делителей и частного от "n" к произведению
            # и удаление одинаковых списков-наборов
            if jj not in res:
                res.append(jj)
            ttemp = sorted([temp,temp1],reverse=True)
            if ttemp not in res:
                res.append(ttemp)
    tt =[n,1]
    res.append(tt)
    res.append(delit)
    ######################################
    minc = int(1e18) + 1
    for i in res :
        j = 0
        ss = 1
        for ii in i:
            ss *= npr[j] ** (ii-1)
            if ss > int(1e18) + 1 :
                ss = int(1e18) + 1
                break
            j += 1
        minc = min(minc,ss)
    print(minc)