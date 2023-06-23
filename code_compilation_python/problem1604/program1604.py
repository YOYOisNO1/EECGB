def program1604():
    Año=int(input())
    while (True):
        Año=Año+1
        A=Año//1000
        B=(Año//100)%10
        C=(Año//10)%10
        D=Año%10
        if (A!=B and A!=C and A!=D and B!=C and B!=D and C!=D):
            break
    print(Año)