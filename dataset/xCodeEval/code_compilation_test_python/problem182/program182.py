def main():
        x: list = list(map(int, input().split()))
        n: int = x[0]
        p: int = x[1]
        k: int = x[2]
        tmp: list = list()
    
        for i in range(k + 1):
            x: int = p - i
            if x is 0:
                break
            elif x is p:
                tmp.append('(' + str(x) + ')')
            else:
                tmp.append(str(x))
    
        tmp.reverse()
    
        if int(tmp[0]) is not 1:
            print('<<', end=' ')
    
        print(' '.join(tmp), end=' ')
        tmp.clear()
    
        for i in range(k + 1):
            x: int = p + i
            if x is n:
                tmp.append(str(x))
                break
            elif x is p:
                continue
            else:
                tmp.append(str(x))
    
        print(' '.join(tmp), end=' ')
    
        if int(tmp[len(tmp) - 1]) is not n:
            print('>>')
    
    
    if __name__ == '__main__':
        main()