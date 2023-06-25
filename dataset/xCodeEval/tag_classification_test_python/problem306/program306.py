def program306():
    p = 10**9 + 7
    
    if __name__ == '__main__':
        s = input()
        # converting "n m k" to integers
        n, m, k = tuple(int(x) for x in s.split())
    
        if k == -1 and (n + m) % 2 == 1:
            print(0)
        else:
            print(pow(2, (n-1) * (m-1), p))