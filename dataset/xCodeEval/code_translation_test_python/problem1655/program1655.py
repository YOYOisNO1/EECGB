def main():
        n, m = map(int, input().split(' '))
        if (n % 2 == 0) and (m % 2 == 0):
            if (n == 2) and (m == 2):
                print(0)
            else:
                print(m*n)
        else:
            if (n % 2 == 1) and (m % 2 == 1):
                if (n == 1) and (m == 1):
                    print(0)
                elif (n == 1) and (m % 6 == 3):
                    print(m - 3)
                elif (n % 6 == 3) and (m == 1):
                    print(n - 3)
                else:
                    print(m*n - 1)
            else:
                if (n == 1) or (m == 1):
                    if (n % 6 == 0) or (m % 6 == 0):
                        print(m*n)
                    else:
                        print(m*n - 2)
                elif (n == 2) or (m == 2):
                    if (n in [3, 7]) or (m in [3, 7]):
                        print(m*n - 2)
                    else:
                        print(m*n)
                else:
                    print(m*n)
    
    
    if __name__ == '__main__':
        main()