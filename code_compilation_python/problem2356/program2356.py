def program2356():
    a = input()
    b = a.split()
    num1 = int(b[0])
    num2 = int(b[1])
    if num1 == num2:
        print('=')
        raise SystemExit(0)
    if num1 > 2 and num2 > 2:
        if num1 > num2:
            print('<')
            raise SystemExit(0)
        else:
            print('>')
            raise SystemExit(0)
    else: 
        if num1 == 1:
            print('<')
            raise SystemExit(0)
        elif num2 == 1:
            print('>')
            raise SystemExit(0)
        else:
            if num1 + num2 <= 5:
                if num1 < num2:
                    print('<')
                    raise SystemExit(0)
                else:
                    print('>')
                    raise SystemExit(0)
            elif num1 + num2 == 6:
                print('=')
                raise SystemExit(0)
            else:
                if num1 > num2:
                    print('<')
                    raise SystemExit(0)
            else:
                print('>')
                raise SystemExit(0)