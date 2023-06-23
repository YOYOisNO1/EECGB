def program2450():
    Квалификация 2, задача: (A) Double Cola, Ошибка исполнения на тесте 1, #
     import sys
    n = sys.stdin.readline()
    crowd = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    k = 5
    if n<=5:
        print crowd[n-1]
    else:
        while n>0:
           n-=k
           k*=2
        k = k/2
        n = n+k
        answer = n/(k/5)
        answer = int(answer)
        print crowd[answer-1]