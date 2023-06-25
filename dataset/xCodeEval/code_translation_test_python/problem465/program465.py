def program465():
    str = input()
    a = int(str[0:str.find(' ')])
    b = int(str[str.find(' '):])
    answ = 1
    if b - a > 4:
        print(0)
    else:
        while b > a:
            answ*= b
            b-=1
        print(answ % 10)