def main():
        n, a, b = int(input()), int(input()), int(input())
        l = [False] * (n + 1)
        l[n % a::a] = [True] * (n // a + 1)
        try:
            i = l[::b].index(True)
            print(f'YES\n{(n-i*b)//a} {i}')
        except ValueError:
            print('NO')
    
    
    if __name__ == '__main__':
        main()