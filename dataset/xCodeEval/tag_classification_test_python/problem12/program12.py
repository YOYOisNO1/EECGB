def program12():
    lista=[int(x) for x in input().split()]
    lista1=[int(x) for x in input().split()]
    a=0
    for i in lista1:
        a+=i
    if (a-max(lista1))>lista[1]:
        print("NO")
    else:
        print("YES")