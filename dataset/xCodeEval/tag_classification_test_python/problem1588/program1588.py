def main():
        a, b = map(int, input().split())
    
        if a == 0 and b == 0:
            print('NO')
        elif abs(b-a) <= 1:
            print('YES')
        else:
            print('NO')
    
    
    if __name__ == '__main__':
        main()