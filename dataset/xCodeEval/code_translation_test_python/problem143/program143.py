def program143():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    op1  = n1 + n2 + n3
    op2 = n1*n2*n3
    op3 = (n1 + n2)*n3
    op4 = n1 * (n2 + n3)
    op5 = n1 * n2 + n3
    op6 = n1 + n2 * n3
    lista = [op1, op2, op3, op4, op5, op6]
    print(max(lista))