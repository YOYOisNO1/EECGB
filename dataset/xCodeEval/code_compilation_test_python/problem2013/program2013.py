def main():
        input()
        w = 10000000
        l = [0] * w
        for m, r in zip(map(int, input().split()), map(int, input().split())):
            l[r:w:m] = [1] * ((w - r + m - 1) // m)
        print(sum(l) / w)
    
    
    if __name__ == '__main__':
        main()