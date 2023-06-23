def frien(arr):
        cont=0
        cont1=0
        cont2 = 0
        cont3 = 0
        cont4 = 0
        cont5 = 0
        cont6 = 0
        cont7 = 0
        cont8 = 0
        cont9 = 0
        cont10 = 0
        aux=0
        arr2=[]
        for i in arr:
            for j in i:
                arr2.append(j)
                if j==0:
                    cont+=1
                    if cont==3:
                        return "WIN"
                elif j==1:
                    cont1+=1
                    if cont1==3:
                        return "WIN"
                elif j==2:
                    cont2+=1
                    if cont2==3:
                        return "WIN"
                elif j==3:
                    cont3+=1
                    if cont3==3:
                        return "WIN"
                elif j==4:
                    cont4+=1
                    if cont4==3:
                        return "WIN"
                elif j==5:
                    cont5+=1
                    if cont5==3:
                        return "WIN"
                elif j==6:
                    cont6+=1
                    if cont6==3:
                        return "WIN"
                elif j==7:
                    cont7+=1
                    if cont7==3:
                        return "WIN"
                elif j==8:
                    cont8+=1
                    if cont8==3:
                        return "WIN"
                elif j==9:
                    cont9+=1
                    if cont9==3:
                        return "WIN"
                else:
                    cont10+=1
                    if cont10==3:
                        return "WIN"
    
        for val in range(min(arr2),max(arr2)):
            if val == 0 and cont==1:
                aux+= 1
                if aux == 3:
                    return "WIN"
            elif j == 1 and cont1==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 2 and cont2==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 3 and cont3==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 4 and cont4==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 5 and cont5==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 6 and cont6==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 7 and cont7==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 8 and cont8==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j == 9 and cont==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            elif j==10 and cont10==1:
                aux += 1
                if aux == 3:
                    return "WIN"
            else:
                continue
    
        return "FAIL"
    
    
    ar=[]
    n = int(input())
    for i in range(n):
        ar.append(list(map(int, input().strip().split())))
    
    print(frien(ar))