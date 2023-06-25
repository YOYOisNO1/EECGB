def program1074():
    for _ in range(int(input())):
        n = int(input())
        if n%2==0:
            print(f'{n/2} {n/2}'
        elif n%3 == 0:
            print(f'{n/3} {n-(n/3)')
        else:
            print(f'1 {n-1})